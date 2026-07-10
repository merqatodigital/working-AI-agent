create table public.policies (
  id uuid primary key default gen_random_uuid(),
  policy_key text unique not null,
  policy_value jsonb not null,
  description text,
  updated_at timestamptz default now()
);

alter table public.policies enable row level security;

create policy "Authenticated users can view policies"
  on public.policies for select
  to authenticated
  using (true);

create policy "Authenticated users can update policies"
  on public.policies for update
  to authenticated
  using (true);
