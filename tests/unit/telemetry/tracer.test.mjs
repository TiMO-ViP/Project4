import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import {
  generateTraceContext,
  createStructuredLog,
  formatStructuredLog,
  parseTraceContext,
  TelemetryTracer,
  generateTraceId,
  generateSpanId,
} from '../../../src/infrastructure/telemetry/tracer.ts';

describe('OpenTelemetry Tracer & Context Propagation Unit Tests', () => {
  describe('generateTraceId and generateSpanId', () => {
    it('should generate valid 32-character hex trace ID', () => {
      const traceId = generateTraceId();
      assert.equal(typeof traceId, 'string');
      assert.equal(traceId.length, 32);
      assert.match(traceId, /^[0-9a-f]{32}$/);
    });

    it('should generate valid 16-character hex span ID', () => {
      const spanId = generateSpanId();
      assert.equal(typeof spanId, 'string');
      assert.equal(spanId.length, 16);
      assert.match(spanId, /^[0-9a-f]{16}$/);
    });
  });

  describe('generateTraceContext', () => {
    it('should generate valid W3C TraceContext header format (00-<trace_id>-<span_id>-01)', () => {
      const header = generateTraceContext();
      assert.equal(typeof header, 'string');
      const parts = header.split('-');
      assert.equal(parts.length, 4);
      assert.equal(parts[0], '00');
      assert.equal(parts[1]?.length, 32);
      assert.equal(parts[2]?.length, 16);
      assert.equal(parts[3], '01');
    });

    it('should respect custom traceId and spanId parameters', () => {
      const customTraceId = '4bf92f3577b34da6a3ce929d0e0e4736';
      const customSpanId = '00f067aa0ba902b7';
      const header = generateTraceContext(customTraceId, customSpanId);
      assert.equal(header, `00-${customTraceId}-${customSpanId}-01`);
    });
  });

  describe('parseTraceContext', () => {
    it('should correctly parse valid W3C TraceContext header', () => {
      const header = '00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01';
      const parsed = parseTraceContext(header);
      assert.notEqual(parsed, null);
      assert.equal(parsed?.traceId, '4bf92f3577b34da6a3ce929d0e0e4736');
      assert.equal(parsed?.spanId, '00f067aa0ba902b7');
      assert.equal(parsed?.sampled, true);
    });

    it('should return null for invalid W3C TraceContext headers', () => {
      assert.equal(parseTraceContext('invalid-header'), null);
      assert.equal(parseTraceContext('01-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01'), null);
      assert.equal(parseTraceContext('00-shorttrace-00f067aa0ba902b7-01'), null);
    });
  });

  describe('Structured JSON Logging', () => {
    it('should produce structured log object with all standard OpenTelemetry fields', () => {
      const traceId = '4bf92f3577b34da6a3ce929d0e0e4736';
      const spanId = '00f067aa0ba902b7';
      const log = createStructuredLog('INFO', 'User authentication succeeded', {
        traceId,
        spanId,
        context: { userId: 'usr-100', ip: '127.0.0.1' },
      });

      assert.equal(log.severity, 'INFO');
      assert.equal(log.message, 'User authentication succeeded');
      assert.equal(log.trace_id, traceId);
      assert.equal(log.span_id, spanId);
      assert.deepEqual(log.context, { userId: 'usr-100', ip: '127.0.0.1' });
      assert.ok(!Number.isNaN(Date.parse(log.timestamp)));
    });

    it('should format structured log as valid JSON string', () => {
      const jsonStr = formatStructuredLog('ERROR', 'Database connection failed', {
        context: { errorCode: 'ECONNREFUSED' },
      });
      const parsed = JSON.parse(jsonStr);
      assert.equal(parsed.severity, 'ERROR');
      assert.equal(parsed.message, 'Database connection failed');
      assert.equal(parsed.context.errorCode, 'ECONNREFUSED');
      assert.equal(typeof parsed.trace_id, 'string');
      assert.equal(typeof parsed.span_id, 'string');
      assert.equal(typeof parsed.timestamp, 'string');
    });
  });

  describe('TelemetryTracer Class', () => {
    it('should instantiate and generate log entries with correlated trace and span IDs', () => {
      const tracer = new TelemetryTracer();
      const traceId = tracer.getTraceId();
      const spanId = tracer.getSpanId();

      assert.equal(traceId.length, 32);
      assert.equal(spanId.length, 16);
      assert.equal(tracer.getTraceContext(), `00-${traceId}-${spanId}-01`);

      const logObj = tracer.info('Service started', { port: 3000 });
      assert.equal(logObj.severity, 'INFO');
      assert.equal(logObj.message, 'Service started');
      assert.equal(logObj.trace_id, traceId);
      assert.equal(logObj.span_id, spanId);
      assert.deepEqual(logObj.context, { port: 3000 });
    });

    it('should support severity convenience methods (info, warn, error, debug)', () => {
      const tracer = new TelemetryTracer('11111111111111111111111111111111', '2222222222222222');

      const infoLog = tracer.info('Info message');
      assert.equal(infoLog.severity, 'INFO');

      const warnLog = tracer.warn('Warn message');
      assert.equal(warnLog.severity, 'WARN');

      const errorLog = tracer.error('Error message');
      assert.equal(errorLog.severity, 'ERROR');

      const debugLog = tracer.debug('Debug message');
      assert.equal(debugLog.severity, 'DEBUG');
    });
  });
});
