create table public.staff (
  id text primary key,
  first_name text not null,
  last_name text not null,
  role text not null,
  department text not null,
  email text,
  phone text,
  shift_schedule jsonb default '{}',
  is_active boolean default true,
  hire_date date,
  created_at timestamptz default now()
);

alter table public.staff enable row level security;

create policy "Authenticated users can view staff"
  on public.staff for select
  to authenticated
  using (true);

create policy "Authenticated users can update staff"
  on public.staff for update
  to authenticated
  using (true);
