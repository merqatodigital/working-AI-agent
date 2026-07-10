create table public.audit_log (
  id uuid primary key default gen_random_uuid(),
  action text not null,
  department text,
  agent_step text,
  details jsonb default '{}',
  guest_id text,
  reservation_id text,
  staff_id text,
  task_id text,
  created_at timestamptz default now()
);

alter table public.audit_log enable row level security;

create policy "Authenticated users can view audit log"
  on public.audit_log for select
  to authenticated
  using (true);

create policy "Authenticated users can insert audit log"
  on public.audit_log for insert
  to authenticated
  with check (true);
