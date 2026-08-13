import { randomBytes } from 'node:crypto';

export type SeverityLevel = 'DEBUG' | 'INFO' | 'WARN' | 'ERROR' | 'FATAL';

export interface StructuredLog {
  timestamp: string;
  trace_id: string;
  span_id: string;
  severity: SeverityLevel;
  message: string;
  context: Record<string, unknown>;
}

export interface LogOptions {
  traceId?: string;
  spanId?: string;
  context?: Record<string, unknown>;
  timestamp?: Date | string;
}

export interface ParsedTraceContext {
  traceId: string;
  spanId: string;
  sampled: boolean;
}

/**
 * Generates a 128-bit (32 hex characters) trace ID in accordance with W3C TraceContext standards.
 */
export function generateTraceId(): string {
  return randomBytes(16).toString('hex');
}

/**
 * Generates a 64-bit (16 hex characters) span ID in accordance with W3C TraceContext standards.
 */
export function generateSpanId(): string {
  return randomBytes(8).toString('hex');
}

/**
 * Generates W3C TraceContext header value (`00-<trace_id>-<span_id>-01`).
 *
 * @param traceId Optional 32-hex character trace ID. If omitted or invalid, a new trace ID is generated.
 * @param spanId Optional 16-hex character span ID. If omitted or invalid, a new span ID is generated.
 * @returns Formatted W3C TraceContext string.
 */
export function generateTraceContext(traceId?: string, spanId?: string): string {
  const validTraceId = traceId && /^[0-9a-fA-F]{32}$/.test(traceId) ? traceId.toLowerCase() : generateTraceId();
  const validSpanId = spanId && /^[0-9a-fA-F]{16}$/.test(spanId) ? spanId.toLowerCase() : generateSpanId();
  return `00-${validTraceId}-${validSpanId}-01`;
}

/**
 * Parses W3C TraceContext header value into trace ID, span ID, and sampled flag.
 *
 * @param header The W3C TraceContext header string.
 * @returns Parsed context or null if header is invalid.
 */
export function parseTraceContext(header: string): ParsedTraceContext | null {
  if (typeof header !== 'string') {
    return null;
  }
  const parts = header.trim().split('-');
  if (parts.length !== 4) {
    return null;
  }
  const version = parts[0];
  const traceId = parts[1];
  const spanId = parts[2];
  const flags = parts[3];

  if (
    version !== '00' ||
    !traceId ||
    traceId.length !== 32 ||
    !/^[0-9a-fA-F]{32}$/.test(traceId) ||
    !spanId ||
    spanId.length !== 16 ||
    !/^[0-9a-fA-F]{16}$/.test(spanId) ||
    !flags ||
    flags.length !== 2
  ) {
    return null;
  }

  return {
    traceId: traceId.toLowerCase(),
    spanId: spanId.toLowerCase(),
    sampled: flags === '01',
  };
}

/**
 * Creates a structured log object containing OpenTelemetry correlation metadata.
 */
export function createStructuredLog(
  severity: SeverityLevel,
  message: string,
  options: LogOptions = {}
): StructuredLog {
  const trace_id = options.traceId && /^[0-9a-fA-F]{32}$/.test(options.traceId)
    ? options.traceId.toLowerCase()
    : generateTraceId();
  const span_id = options.spanId && /^[0-9a-fA-F]{16}$/.test(options.spanId)
    ? options.spanId.toLowerCase()
    : generateSpanId();

  let timestampStr: string;
  if (options.timestamp instanceof Date) {
    timestampStr = options.timestamp.toISOString();
  } else if (typeof options.timestamp === 'string') {
    timestampStr = options.timestamp;
  } else {
    timestampStr = new Date().toISOString();
  }

  return {
    timestamp: timestampStr,
    trace_id,
    span_id,
    severity,
    message,
    context: options.context ?? {},
  };
}

/**
 * Formats a structured log as a JSON string.
 */
export function formatStructuredLog(
  severity: SeverityLevel,
  message: string,
  options: LogOptions = {}
): string {
  return JSON.stringify(createStructuredLog(severity, message, options));
}

/**
 * TelemetryTracer manages active trace and span correlation context across application operations.
 */
export class TelemetryTracer {
  private currentTraceId: string;
  private currentSpanId: string;

  constructor(traceId?: string, spanId?: string) {
    this.currentTraceId = traceId && /^[0-9a-fA-F]{32}$/.test(traceId)
      ? traceId.toLowerCase()
      : generateTraceId();
    this.currentSpanId = spanId && /^[0-9a-fA-F]{16}$/.test(spanId)
      ? spanId.toLowerCase()
      : generateSpanId();
  }

  public getTraceId(): string {
    return this.currentTraceId;
  }

  public getSpanId(): string {
    return this.currentSpanId;
  }

  public getTraceContext(): string {
    return generateTraceContext(this.currentTraceId, this.currentSpanId);
  }

  public log(severity: SeverityLevel, message: string, context: Record<string, unknown> = {}): StructuredLog {
    return createStructuredLog(severity, message, {
      traceId: this.currentTraceId,
      spanId: this.currentSpanId,
      context,
    });
  }

  public info(message: string, context?: Record<string, unknown>): StructuredLog {
    return this.log('INFO', message, context);
  }

  public warn(message: string, context?: Record<string, unknown>): StructuredLog {
    return this.log('WARN', message, context);
  }

  public error(message: string, context?: Record<string, unknown>): StructuredLog {
    return this.log('ERROR', message, context);
  }

  public debug(message: string, context?: Record<string, unknown>): StructuredLog {
    return this.log('DEBUG', message, context);
  }
}
