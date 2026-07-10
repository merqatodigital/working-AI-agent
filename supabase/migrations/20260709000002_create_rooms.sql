create table public.rooms (
  id text primary key,
  room_number text unique not null,
  room_type text not null default 'standard',
  floor int default 1,
  status text default 'available',
  base_rate numeric(10,2) not null,
  current_rate numeric(10,2),
  amenities jsonb default '[]',
  last_cleaned_at timestamptz,
  maintenance_notes text,
  created_at timestamptz default now()
);

alter table public.rooms enable row level security;

create policy "Authenticated users can view rooms"
  on public.rooms for select
  to authenticated
  using (true);

create policy "Authenticated users can update rooms"
  on public.rooms for update
  to authenticated
  using (true);
