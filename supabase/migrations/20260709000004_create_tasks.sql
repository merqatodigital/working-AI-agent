create table public.tasks (
  id text primary key,
  department text not null,
  title text not null,
  description text,
  priority text default 'normal',
  status text default 'pending',
  assigned_to text references public.staff(id),
  room_id text references public.rooms(id),
  guest_id text references public.guests(id),
  reservation_id text references public.reservations(id),
  created_at timestamptz default now(),
  started_at timestamptz,
  completed_at timestamptz,
  completion_notes text,
  created_by text default 'agent'
);

alter table public.tasks enable row level security;

create policy "Authenticated users can view tasks"
  on public.tasks for select
  to authenticated
  using (true);

create policy "Authenticated users can insert tasks"
  on public.tasks for insert
  to authenticated
  with check (true);

create policy "Authenticated users can update tasks"
  on public.tasks for update
  to authenticated
  using (true);
