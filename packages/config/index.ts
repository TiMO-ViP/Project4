/**
 * Global enterprise application configuration and environment constants.
 */

export const LOG_LEVEL = {
  DEBUG: 'debug',
  INFO: 'info',
  WARN: 'warn',
  ERROR: 'error',
} as const;

export type LogLevel = (typeof LOG_LEVEL)[keyof typeof LOG_LEVEL];

export const ENVIRONMENT_STAGES = {
  DEVELOPMENT: 'development',
  STAGING: 'staging',
  PRODUCTION: 'production',
  TEST: 'test',
} as const;

export type EnvironmentStage = (typeof ENVIRONMENT_STAGES)[keyof typeof ENVIRONMENT_STAGES];

export const APP_CONFIG = {
  name: 'Project4 Enterprise App',
  version: '2026.1.0',
  defaultStage: ENVIRONMENT_STAGES.DEVELOPMENT,
  defaultLogLevel: LOG_LEVEL.INFO,
  apiPrefix: '/api/v1',
} as const;

export type AppConfig = typeof APP_CONFIG;
