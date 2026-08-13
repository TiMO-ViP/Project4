/**
 * Shared enterprise type definitions across monorepo packages.
 */

export interface BaseEntityProps {
  id: string;
  createdAt: Date;
  updatedAt: Date;
  deletedAt?: Date | null;
}

export interface PaginationMeta {
  page: number;
  limit: number;
  totalItems: number;
  totalPages: number;
  hasNextPage: boolean;
  hasPreviousPage: boolean;
}

export interface ApiResponse<T = unknown> {
  success: boolean;
  data?: T;
  error?: string;
  meta?: PaginationMeta;
  timestamp: string;
}

export type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };
