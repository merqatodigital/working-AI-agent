create table public.approvals (
  id text primary key,
  approval_type text not null,
  action_type text not null,
  action_payload jsonb not null,
  status text default 'pending',
  requested_by text default 'agent',
  reviewed_by text,
  reviewed_at timestamptz,
  notes text,
  created_at timestamptz default now()
);

alter table public.approvals enable row level security;

create policy "Authenticated users can view approvals"
  on public.approvals for select
  to authenticated
  using (true);

create policy "Authenticated users can insert approvals"
  on public.approvals for insert
  to authenticated
  with check (true);

create policy "Authenticated users can update approvals"
  on public.approvals for update
  to authenticated
  using (true);
