import { defineConfig } from 'drizzle-kit';

// Default to local PostgreSQL container (Port 54322) to prevent accidental cloud mutations.
const isCloud = process.env.DB_TARGET === 'cloud';
const dbUrl = isCloud
  ? process.env.SUPABASE_CLOUD_DATABASE_URL || process.env.DATABASE_URL
  : process.env.LOCAL_DATABASE_URL || 'postgresql://postgres:postgres@127.0.0.1:54322/postgres';

export default defineConfig({
  schema: './src/db/schema.ts',
  out: './supabase/migrations',
  dialect: 'postgresql',
  dbCredentials: {
    url: dbUrl || 'postgresql://postgres:postgres@127.0.0.1:54322/postgres',
  },
  verbose: true,
  strict: true,
});
