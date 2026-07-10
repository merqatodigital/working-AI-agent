create table public.inventory (
  id text primary key,
  item_name text not null,
  category text not null,
  current_quantity int default 0,
  min_quantity int default 10,
  unit text default 'units',
  unit_cost numeric(10,2) default 0,
  supplier text,
  last_restocked_at timestamptz,
  created_at timestamptz default now()
);

alter table public.inventory enable row level security;

create policy "Authenticated users can view inventory"
  on public.inventory for select
  to authenticated
  using (true);

create policy "Authenticated users can update inventory"
  on public.inventory for update
  to authenticated
  using (true);
