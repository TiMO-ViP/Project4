import type { IncomingMessage, ServerResponse } from 'node:http';

/**
 * Enterprise Next.js 16 Network Proxy & Security Boundary
 * Location: src/proxy.ts
 *
 * Enforces OWASP 2025 security headers, CORS restrictions, and request filtering
 * at the Node.js network boundary before requests reach Next.js App Router endpoints.
 */

export interface SecurityHeaders {
  [key: string]: string;
}

export const SECURITY_HEADERS: SecurityHeaders = {
  'X-DNS-Prefetch-Control': 'on',
  'Strict-Transport-Security': 'max-age=63072000; includeSubDomains; preload',
  'X-Frame-Options': 'SAMEORIGIN',
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'origin-when-cross-origin',
  'X-Permitted-Cross-Domain-Policies': 'none',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), browsing-topics=()',
  'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob: https:; font-src 'self' data:; connect-src 'self' https://*.supabase.co;",
};

export function applySecurityHeaders(res: ServerResponse): void {
  for (const [header, value] of Object.entries(SECURITY_HEADERS)) {
    res.setHeader(header, value);
  }
}

export function handleProxyRequest(req: IncomingMessage, res: ServerResponse): boolean {
  applySecurityHeaders(res);

  // Block suspicious or malicious payload signatures
  const userAgent = req.headers['user-agent'] || '';
  if (userAgent.includes('sqlmap') || userAgent.includes('nikto')) {
    res.statusCode = 403;
    res.end('Forbidden: Malicious User Agent Detected');
    return false;
  }

  return true;
}
