create table public.reservations (
  id text primary key,
  guest_id text references public.guests(id),
  room_id text,
  check_in_date date not null,
  check_out_date date not null,
  status text default 'confirmed',
  room_type text default 'standard',
  adults int default 1,
  children int default 0,
  total_amount numeric(10,2),
  paid_amount numeric(10,2) default 0,
  notes text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

alter table public.reservations enable row level security;

create policy "Authenticated users can view reservations"
  on public.reservations for select
  to authenticated
  using (true);

create policy "Authenticated users can insert reservations"
  on public.reservations for insert
  to authenticated
  with check (true);

create policy "Authenticated users can update reservations"
  on public.reservations for update
  to authenticated
  using (true);
