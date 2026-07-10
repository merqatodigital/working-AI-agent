create table public.guests (
  id text primary key,
  first_name text not null,
  last_name text not null,
  email text unique,
  phone text,
  nationality text,
  preferences jsonb default '{}',
  past_stays jsonb default '[]',
  loyalty_tier text default 'standard',
  notes text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

alter table public.guests enable row level security;

create policy "Authenticated users can view guests"
  on public.guests for select
  to authenticated
  using (true);

create policy "Authenticated users can insert guests"
  on public.guests for insert
  to authenticated
  with check (true);

create policy "Authenticated users can update guests"
  on public.guests for update
  to authenticated
  using (true);
