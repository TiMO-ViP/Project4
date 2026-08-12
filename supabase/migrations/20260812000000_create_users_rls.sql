-- Enable Row-Level Security (RLS) on public.users
ALTER TABLE IF EXISTS public.users ENABLE ROW LEVEL SECURITY;

-- 1. SELECT Policy: Authenticated users can view their own profile
CREATE POLICY "users_select_own_profile"
ON public.users
FOR SELECT
TO authenticated
USING ( (select auth.uid())::text = id );

-- 2. INSERT Policy: Authenticated users can insert their own profile
CREATE POLICY "users_insert_own_profile"
ON public.users
FOR INSERT
TO authenticated
WITH CHECK ( (select auth.uid())::text = id );

-- 3. UPDATE Policy: Requires BOTH USING and WITH CHECK to prevent ID hijacking
CREATE POLICY "users_update_own_profile"
ON public.users
FOR UPDATE
TO authenticated
USING ( (select auth.uid())::text = id )
WITH CHECK ( (select auth.uid())::text = id );
