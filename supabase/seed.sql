-- KAPWA Resort OS seed data
-- Run after all migrations: supabase db seed

-- Guests
insert into public.guests (id, first_name, last_name, email, phone, nationality, preferences, past_stays, loyalty_tier, notes) values
('G001', 'Maria', 'Santos', 'maria@email.com', '+63-917-123-4567', 'Philippine', '{"room_view": "ocean", "dietary": "vegetarian"}', '[{"date": "2025-12-20", "room": "R301", "rating": 5}]', 'gold', 'Regular guest, prefers quiet rooms'),
('G002', 'John', 'Smith', 'john@email.com', '+1-555-0123', 'American', '{"room_view": "garden", "pillow": "firm"}', '[]', 'standard', null),
('G003', 'Yuki', 'Tanaka', 'yuki@email.com', '+81-90-1234-5678', 'Japanese', '{"room_view": "ocean", "quiet_room": true}', '[{"date": "2026-01-15", "room": "R205", "rating": 4}]', 'silver', 'Prefers Japanese-speaking staff if available'),
('G004', 'Hans', 'Mueller', 'hans@email.com', '+49-170-1234567', 'German', '{"room_view": "pool"}', '[]', 'standard', null),
('G005', 'Ana', 'Garcia', 'ana@email.com', '+34-612-345-678', 'Spanish', '{"dietary": "gluten_free"}', '[{"date": "2025-06-10", "room": "V102", "rating": 5}, {"date": "2025-11-22", "room": "R303", "rating": 4}]', 'gold', 'VIP guest, always celebrates anniversary here'),
('G006', 'Chen', 'Wei', 'chen@email.com', '+86-138-0013-8000', 'Chinese', '{"language": "Mandarin"}', '[]', 'standard', null),
('G007', 'Sarah', 'Johnson', 'sarah@email.com', '+44-7911-123456', 'British', '{"room_view": "ocean", "late_checkout": true}', '[{"date": "2026-03-05", "room": "R208", "rating": 5}]', 'silver', 'Travel blogger, good for reviews'),
('G008', 'Raj', 'Patel', 'raj@email.com', '+91-98765-43210', 'Indian', '{"dietary": "vegetarian"}', '[]', 'standard', null),
('G009', 'Emma', 'Brown', 'emma@email.com', '+61-412-345-678', 'Australian', '{"adventure_activities": true}', '[]', 'standard', 'Interested in island hopping and diving'),
('G010', 'Carlos', 'Rivera', 'carlos@email.com', '+52-55-1234-5678', 'Mexican', '{"language": "Spanish"}', '[{"date": "2025-08-18", "room": "V104", "rating": 5}]', 'gold', 'Honeymoon guest, book flowers on arrival');

-- Staff
insert into public.staff (id, first_name, last_name, role, department, email, phone, shift_schedule, is_active, hire_date) values
('S001', 'Ricardo', 'Dela Cruz', 'Manager', 'front_desk', 'ricardo@resort.com', '+63-917-000-0001', '{"mon": "07:00-15:00", "tue": "07:00-15:00", "wed": "07:00-15:00", "thu": "07:00-15:00", "fri": "07:00-15:00", "sat": "07:00-15:00", "sun": "off"}', true, '2020-01-15'),
('S002', 'Maria', 'Reyes', 'Front Desk Agent', 'front_desk', 'maria.r@resort.com', '+63-917-000-0002', '{"mon": "07:00-15:00", "tue": "07:00-15:00", "wed": "off", "thu": "07:00-15:00", "fri": "07:00-15:00", "sat": "off", "sun": "07:00-15:00"}', true, '2022-03-01'),
('S003', 'Jose', 'Villanueva', 'Housekeeping Lead', 'housekeeping', 'jose@resort.com', '+63-917-000-0003', '{"mon": "06:00-14:00", "tue": "06:00-14:00", "wed": "06:00-14:00", "thu": "06:00-14:00", "fri": "06:00-14:00", "sat": "06:00-14:00", "sun": "off"}', true, '2019-06-15'),
('S004', 'Anna', 'Santos', 'Housekeeping Attendant', 'housekeeping', 'anna@resort.com', '+63-917-000-0004', '{"mon": "06:00-14:00", "tue": "off", "wed": "06:00-14:00", "thu": "06:00-14:00", "fri": "off", "sat": "06:00-14:00", "sun": "06:00-14:00"}', true, '2023-01-10'),
('S005', 'Miguel', 'Torres', 'Maintenance Technician', 'maintenance', 'miguel@resort.com', '+63-917-000-0005', '{"mon": "08:00-16:00", "tue": "08:00-16:00", "wed": "08:00-16:00", "thu": "08:00-16:00", "fri": "08:00-16:00", "sat": "off", "sun": "off"}', true, '2021-04-20'),
('S006', 'Pedro', 'Garcia', 'Maintenance Helper', 'maintenance', 'pedro@resort.com', '+63-917-000-0006', '{"mon": "08:00-16:00", "tue": "08:00-16:00", "wed": "off", "thu": "08:00-16:00", "fri": "08:00-16:00", "sat": "08:00-16:00", "sun": "off"}', true, '2023-09-01'),
('S007', 'Lisa', 'Chen', 'Reservations Agent', 'reservations', 'lisa@resort.com', '+63-917-000-0007', '{"mon": "09:00-17:00", "tue": "09:00-17:00", "wed": "09:00-17:00", "thu": "09:00-17:00", "fri": "09:00-17:00", "sat": "off", "sun": "off"}', true, '2022-07-15'),
('S008', 'David', 'Williams', 'Guest Relations', 'guest_relations', 'david@resort.com', '+63-917-000-0008', '{"mon": "08:00-16:00", "tue": "08:00-16:00", "wed": "08:00-16:00", "thu": "off", "fri": "08:00-16:00", "sat": "08:00-16:00", "sun": "08:00-16:00"}', true, '2021-11-01'),
('S009', 'Sofia', 'Rodriguez', 'Guest Relations', 'guest_relations', 'sofia@resort.com', '+63-917-000-0009', '{"mon": "off", "tue": "08:00-16:00", "wed": "08:00-16:00", "thu": "08:00-16:00", "fri": "08:00-16:00", "sat": "08:00-16:00", "sun": "08:00-16:00"}', true, '2023-02-15'),
('S010', 'Marco', 'Lim', 'Inventory Clerk', 'inventory', 'marco@resort.com', '+63-917-000-0010', '{"mon": "08:00-16:00", "tue": "08:00-16:00", "wed": "08:00-16:00", "thu": "08:00-16:00", "fri": "08:00-16:00", "sat": "off", "sun": "off"}', true, '2022-05-10'),
('S011', 'Teresa', 'Cruz', 'Accountant', 'finance', 'teresa@resort.com', '+63-917-000-0011', '{"mon": "09:00-17:00", "tue": "09:00-17:00", "wed": "09:00-17:00", "thu": "09:00-17:00", "fri": "09:00-17:00", "sat": "off", "sun": "off"}', true, '2020-08-01'),
('S012', 'James', 'Brown', 'Security', 'front_desk', 'james@resort.com', '+63-917-000-0012', '{"mon": "22:00-06:00", "tue": "22:00-06:00", "wed": "22:00-06:00", "thu": "22:00-06:00", "fri": "22:00-06:00", "sat": "22:00-06:00", "sun": "22:00-06:00"}', true, '2021-03-15');

-- Rooms
insert into public.rooms (id, room_number, room_type, floor, status, base_rate, amenities, last_cleaned_at, maintenance_notes) values
('R001', 'R101', 'standard', 1, 'available', 3500, '["ac", "wifi", "tv"]', '2026-07-08T10:00:00', null),
('R002', 'R102', 'standard', 1, 'occupied', 3500, '["ac", "wifi", "tv"]', '2026-07-03T14:00:00', 'AC intermittent, monitor'),
('R003', 'R103', 'standard', 1, 'available', 3500, '["ac", "wifi", "tv"]', '2026-07-08T11:00:00', null),
('R004', 'R104', 'standard', 1, 'cleaning', 3500, '["ac", "wifi", "tv"]', null, null),
('R005', 'R105', 'standard', 1, 'available', 3500, '["ac", "wifi", "tv"]', '2026-07-08T09:00:00', null),
('R006', 'R201', 'deluxe', 2, 'occupied', 5500, '["ac", "wifi", "tv", "minibar", "balcony"]', '2026-07-08T08:00:00', null),
('R007', 'R202', 'deluxe', 2, 'available', 5500, '["ac", "wifi", "tv", "minibar", "balcony"]', '2026-07-08T10:30:00', null),
('R008', 'R203', 'deluxe', 2, 'maintenance', 5500, '["ac", "wifi", "tv", "minibar", "balcony"]', '2026-07-05T10:00:00', 'Bathroom faucet leaking, parts ordered'),
('R009', 'R204', 'deluxe', 2, 'available', 5500, '["ac", "wifi", "tv", "minibar", "balcony"]', '2026-07-08T11:00:00', null),
('R010', 'R205', 'deluxe', 2, 'available', 5500, '["ac", "wifi", "tv", "minibar", "balcony"]', '2026-07-08T10:00:00', null),
('R011', 'R206', 'deluxe', 2, 'occupied', 5500, '["ac", "wifi", "tv", "minibar", "balcony"]', '2026-07-05T14:00:00', null),
('R012', 'R207', 'deluxe', 2, 'available', 5500, '["ac", "wifi", "tv", "minibar", "balcony"]', '2026-07-08T09:30:00', null),
('R013', 'R208', 'deluxe', 2, 'occupied', 5500, '["ac", "wifi", "tv", "minibar", "balcony"]', '2026-07-06T14:00:00', null),
('R014', 'R209', 'deluxe', 2, 'available', 5500, '["ac", "wifi", "tv", "minibar", "balcony"]', '2026-07-08T10:00:00', null),
('R015', 'R210', 'deluxe', 2, 'cleaning', 5500, '["ac", "wifi", "tv", "minibar", "balcony"]', null, null),
('R016', 'R301', 'suite', 3, 'occupied', 8500, '["ac", "wifi", "tv", "minibar", "balcony", "jacuzzi", "ocean_view"]', '2026-07-01T14:00:00', null),
('R017', 'R302', 'suite', 3, 'available', 8500, '["ac", "wifi", "tv", "minibar", "balcony", "jacuzzi", "ocean_view"]', '2026-07-08T11:00:00', null),
('R018', 'R303', 'suite', 3, 'available', 8500, '["ac", "wifi", "tv", "minibar", "balcony", "jacuzzi", "ocean_view"]', '2026-07-08T10:00:00', null),
('R019', 'R304', 'suite', 3, 'occupied', 8500, '["ac", "wifi", "tv", "minibar", "balcony", "jacuzzi", "ocean_view"]', '2026-07-07T10:00:00', null),
('R020', 'R305', 'suite', 3, 'available', 8500, '["ac", "wifi", "tv", "minibar", "balcony", "jacuzzi", "ocean_view"]', '2026-07-08T09:00:00', null),
('R021', 'R306', 'suite', 3, 'maintenance', 8500, '["ac", "wifi", "tv", "minibar", "balcony", "jacuzzi", "ocean_view"]', '2026-07-04T10:00:00', 'Jacuzzi motor replacement in progress'),
('R022', 'R307', 'suite', 3, 'available', 8500, '["ac", "wifi", "tv", "minibar", "balcony", "jacuzzi", "ocean_view"]', '2026-07-08T10:30:00', null),
('R023', 'R308', 'suite', 3, 'occupied', 8500, '["ac", "wifi", "tv", "minibar", "balcony", "jacuzzi", "ocean_view"]', '2026-07-06T10:00:00', null),
('R024', 'R309', 'suite', 3, 'available', 8500, '["ac", "wifi", "tv", "minibar", "balcony", "jacuzzi", "ocean_view"]', '2026-07-08T11:00:00', null),
('R025', 'R310', 'suite', 3, 'available', 8500, '["ac", "wifi", "tv", "minibar", "balcony", "jacuzzi", "ocean_view"]', '2026-07-08T10:00:00', null),
('R026', 'V101', 'villa', 0, 'occupied', 15000, '["ac", "wifi", "tv", "minibar", "private_pool", "ocean_view", "kitchen"]', '2026-07-10T14:00:00', null),
('R027', 'V102', 'villa', 0, 'available', 15000, '["ac", "wifi", "tv", "minibar", "private_pool", "ocean_view", "kitchen"]', '2026-07-08T10:00:00', null),
('R028', 'V103', 'villa', 0, 'available', 15000, '["ac", "wifi", "tv", "minibar", "private_pool", "ocean_view", "kitchen"]', '2026-07-08T11:00:00', null),
('R029', 'V104', 'villa', 0, 'occupied', 15000, '["ac", "wifi", "tv", "minibar", "private_pool", "ocean_view", "kitchen"]', '2026-07-08T08:00:00', null),
('R030', 'V105', 'villa', 0, 'available', 15000, '["ac", "wifi", "tv", "minibar", "private_pool", "ocean_view", "kitchen"]', '2026-07-08T09:00:00', null);

-- Reservations
insert into public.reservations (id, guest_id, room_id, check_in_date, check_out_date, status, room_type, adults, children, total_amount, paid_amount, notes) values
('RES001', 'G001', 'R016', '2026-07-01', '2026-07-05', 'checked_in', 'suite', 2, 0, 34000, 34000, 'Anniversary trip'),
('RES002', 'G002', 'R002', '2026-07-03', '2026-07-07', 'checked_in', 'standard', 1, 0, 14000, 14000, null),
('RES003', 'G003', 'R006', '2026-07-08', '2026-07-12', 'checked_in', 'deluxe', 2, 1, 22000, 11000, 'Early check-in requested'),
('RES004', 'G005', 'R026', '2026-07-10', '2026-07-15', 'confirmed', 'villa', 2, 0, 75000, 37500, 'Anniversary celebration, arrange flowers'),
('RES005', 'G004', 'R011', '2026-07-05', '2026-07-09', 'checked_in', 'deluxe', 1, 0, 22000, 22000, null),
('RES006', 'G007', 'R013', '2026-07-06', '2026-07-10', 'checked_in', 'deluxe', 1, 0, 22000, 22000, 'Late checkout requested'),
('RES007', 'G009', 'R005', '2026-07-12', '2026-07-16', 'confirmed', 'standard', 2, 0, 14000, 7000, 'Wants island hopping tour info');

-- Inventory
insert into public.inventory (id, item_name, category, current_quantity, min_quantity, unit, unit_cost, supplier, last_restocked_at) values
('INV001', 'Bath Towels', 'linens', 150, 50, 'pieces', 250, 'Palawan Linens Supply', '2026-07-01'),
('INV002', 'Bed Sheets (King)', 'linens', 45, 20, 'sets', 450, 'Palawan Linens Supply', '2026-06-15'),
('INV003', 'Bed Sheets (Queen)', 'linens', 38, 20, 'sets', 380, 'Palawan Linens Supply', '2026-06-15'),
('INV004', 'Shampoo Bottles', 'toiletries', 300, 100, 'bottles', 35, 'Manila Toiletries Co.', '2026-07-01'),
('INV005', 'Conditioner Bottles', 'toiletries', 280, 100, 'bottles', 35, 'Manila Toiletries Co.', '2026-07-01'),
('INV006', 'Soap Bars', 'toiletries', 400, 150, 'pieces', 15, 'Manila Toiletries Co.', '2026-07-01'),
('INV007', 'Body Lotion', 'toiletries', 180, 80, 'bottles', 45, 'Manila Toiletries Co.', '2026-06-20'),
('INV008', 'Pool Towels', 'linens', 80, 30, 'pieces', 180, 'Palawan Linens Supply', '2026-07-01'),
('INV009', 'Coffee Pods', 'minibar', 500, 100, 'pieces', 8, 'Davao Coffee Roasters', '2026-07-05'),
('INV010', 'Mini Water Bottles', 'minibar', 200, 50, 'bottles', 12, 'Palawan Water Co.', '2026-07-05'),
('INV011', 'Tea Bags', 'minibar', 300, 80, 'pieces', 5, 'Davao Coffee Roasters', '2026-07-05'),
('INV012', 'Cleaning Spray', 'cleaning', 25, 10, 'bottles', 65, 'Cebu Clean Supplies', '2026-06-25'),
('INV013', 'Laundry Detergent', 'cleaning', 18, 8, 'bottles', 85, 'Cebu Clean Supplies', '2026-06-25'),
('INV014', 'Vacuum Bags', 'cleaning', 15, 5, 'pieces', 120, 'Cebu Clean Supplies', '2026-06-10'),
('INV015', 'Light Bulbs', 'maintenance', 40, 15, 'pieces', 45, 'Manila Hardware', '2026-06-01'),
('INV016', 'Air Filters', 'maintenance', 8, 6, 'pieces', 350, 'Manila Hardware', '2026-05-15'),
('INV017', 'Plunger', 'maintenance', 5, 3, 'pieces', 150, 'Manila Hardware', '2026-04-20'),
('INV018', 'Duct Tape', 'maintenance', 12, 5, 'rolls', 60, 'Manila Hardware', '2026-06-01'),
('INV019', 'Welcome Drink Mix', 'minibar', 60, 30, 'portions', 25, 'Palawan Beverages', '2026-07-01'),
('INV020', 'Bath Robes', 'linens', 35, 15, 'pieces', 500, 'Palawan Linens Supply', '2026-06-10');

-- Policies
insert into public.policies (policy_key, policy_value, description) values
('checkout_time', '"12:00"', 'Standard checkout time'),
('late_checkout', '{"allowed_hours": 3, "fee_php": 1500, "requires_approval": false}', 'Late checkout policy'),
('cancellation_policy', '{"full_refund_before_hours": 48, "partial_refund_before_hours": 24, "partial_refund_percent": 50, "no_refund_after_hours": 24}', 'Cancellation refund tiers'),
('approval_limits', '{"staff": 5000, "supervisor": 25000, "manager": 100000, "owner": 999999}', 'Approval authority by role'),
('currency', '"PHP"', 'Philippine Peso'),
('tax_rate', '{"vat_percent": 12, "service_charge_percent": 10}', 'Taxes and service charges'),
('resort_info', '{"name": "KAPWA Beach Resort", "location": "Palawan Island, Philippines", "total_rooms": 30, "total_villas": 5, "check_in_time": "14:00", "pool_hours": "07:00-22:00", "restaurant_hours": "06:30-22:00", "spa_hours": "09:00-20:00", "emergency_number": "+63-917-000-9999"}', 'Resort information');
