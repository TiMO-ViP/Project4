export default function HomePage() {
  return (
    <div style={{ padding: '3rem', maxWidth: '1200px', margin: '0 auto' }}>
      <header style={{ marginBottom: '2rem', borderBottom: '1px solid var(--card-border)', paddingBottom: '1rem' }}>
        <h1 style={{ fontSize: '2.25rem', fontWeight: 700 }}>Project4 Enterprise Platform</h1>
        <p style={{ color: 'var(--muted)', marginTop: '0.5rem' }}>
          Next.js 16 App Router • Supabase Cloud & Local • Drizzle ORM • Clean Architecture
        </p>
      </header>

      <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1.5rem' }}>
        <div style={{ background: 'var(--card)', border: '1px solid var(--card-border)', borderRadius: '8px', padding: '1.5rem' }}>
          <h2 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>⚡ Architecture</h2>
          <p style={{ color: 'var(--muted)', fontSize: '0.875rem' }}>
            Domain-Driven Design (DDD) with pure business entities, application services, and infrastructure adapters.
          </p>
        </div>

        <div style={{ background: 'var(--card)', border: '1px solid var(--card-border)', borderRadius: '8px', padding: '1.5rem' }}>
          <h2 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>🗄️ Database & RLS</h2>
          <p style={{ color: 'var(--muted)', fontSize: '0.875rem' }}>
            Supabase Postgres with Row-Level Security, B-Tree indexes, and Drizzle ORM schema isolation.
          </p>
        </div>

        <div style={{ background: 'var(--card)', border: '1px solid var(--card-border)', borderRadius: '8px', padding: '1.5rem' }}>
          <h2 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>🔒 Security & Proxy</h2>
          <p style={{ color: 'var(--muted)', fontSize: '0.875rem' }}>
            OWASP 2025 security headers, Node.js proxy boundary filter, and automated Gitleaks secret protection.
          </p>
        </div>
      </section>
    </div>
  );
}
