import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Project4 — Enterprise Modular Platform',
  description: 'Next.js 16, Clean Architecture, Supabase & Drizzle ORM Multi-Stack Platform',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <main>{children}</main>
      </body>
    </html>
  );
}
