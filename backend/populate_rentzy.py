import asyncio
import random
from datetime import datetime, timezone
from app.db.mongo import get_db
from app.core.security import hash_password

CATEGORIES = [
    {"name": "Electronics & Gadgets", "slug": "electronics-gadgets", "icon": "devices", "active": True},
    {"name": "Bikes", "slug": "bikes", "icon": "two_wheeler", "active": True},
    {"name": "Cars", "slug": "cars", "icon": "directions_car", "active": True},
    {"name": "Rooms", "slug": "rooms", "icon": "meeting_room", "active": True},
    {"name": "PG Accommodations", "slug": "pg-accommodations", "icon": "bed", "active": True},
    {"name": "Houses", "slug": "houses", "icon": "home", "active": True},
    {"name": "Apartments", "slug": "apartments", "icon": "apartment", "active": True},
    {"name": "Land", "slug": "land", "icon": "terrain", "active": True},
    {"name": "Event & Party Equipment", "slug": "event-party-equipment", "icon": "celebration", "active": True},
    {"name": "Sports & Fitness Equipment", "slug": "sports-fitness-equipment", "icon": "fitness_center", "active": True},
    {"name": "Travel & Camping Gear", "slug": "travel-camping-gear", "icon": "camping", "active": True},
    {"name": "Furniture", "slug": "furniture", "icon": "chair", "active": True},
    {"name": "Home Appliances", "slug": "home-appliances", "icon": "kitchen", "active": True},
    {"name": "Tools", "slug": "tools", "icon": "build", "active": True},
    {"name": "Construction Equipment", "slug": "construction-equipment", "icon": "construction", "active": True},
    {"name": "Fashion & Occasion Wear", "slug": "fashion-occasion-wear", "icon": "checkroom", "active": True},
    {"name": "Gaming Equipment", "slug": "gaming-equipment", "icon": "sports_esports", "active": True},
    {"name": "Industrial Machinery", "slug": "industrial-machinery", "icon": "precision_manufacturing", "active": True},
    {"name": "Gardening Tools", "slug": "gardening-tools", "icon": "yard", "active": True},
    {"name": "Content Creation Equipment", "slug": "content-creation-equipment", "icon": "videocam", "active": True},
    {"name": "Office & Business Equipment", "slug": "office-business-equipment", "icon": "print", "active": True},
    {"name": "Musical Instruments", "slug": "musical-instruments", "icon": "music_note", "active": True},
    {"name": "Hobby-Related Items", "slug": "hobby-related-items", "icon": "palette", "active": True},
    {"name": "Luxury Products", "slug": "luxury-products", "icon": "diamond", "active": True},
    {"name": "Temporary Business Setups", "slug": "temporary-business-setups", "icon": "storefront", "active": True},
]

DEMO_USERS = [
    # 1 Admin
    {
        "name": "Rajesh Kumar (Rentzy Admin)",
        "email": "admin.rajesh@rentzy.com",
        "phone": "+919876543210",
        "password": "Password@123",
        "role": "admin",
        "kyc_status": "verified",
        "trust_score": 100,
        "bio": "Rentzy Senior Operations & Trust Director"
    },
    # 3 Owners
    {
        "name": "Aarav Sharma (Elite Equipment Rentals)",
        "email": "owner.aarav@rentzy.com",
        "phone": "+919811223344",
        "password": "Password@123",
        "role": "owner",
        "kyc_status": "verified",
        "trust_score": 96,
        "bio": "Specializing in premium gadgets, cinema cameras, mobility, and industrial tools across Bangalore & Coimbatore."
    },
    {
        "name": "Priya Nair (UrbanSpaces & Living Hub)",
        "email": "owner.priya@rentzy.com",
        "phone": "+919822334455",
        "password": "Password@123",
        "role": "owner",
        "kyc_status": "verified",
        "trust_score": 94,
        "bio": "Verified host offering vetted studio apartments, luxury stays, event spaces, and high-end furniture."
    },
    {
        "name": "Karthik Verma (Velocity & Craft Gear)",
        "email": "owner.karthik@rentzy.com",
        "phone": "+919833445566",
        "password": "Password@123",
        "role": "owner",
        "kyc_status": "verified",
        "trust_score": 92,
        "bio": "Commercial fleet operator, adventure & camping curator, gaming rigs and industrial tools provider."
    },
    # 3 Customers
    {
        "name": "Ananya Iyer (Filmmaker & Creator)",
        "email": "customer.ananya@rentzy.com",
        "phone": "+919844556677",
        "password": "Password@123",
        "role": "customer",
        "kyc_status": "verified",
        "trust_score": 95,
        "bio": "Independent documentary producer frequently renting creative and travel setups."
    },
    {
        "name": "Rohan Deshmukh (Tech Consultant & Nomad)",
        "email": "customer.rohan@rentzy.com",
        "phone": "+919855667788",
        "password": "Password@123",
        "role": "customer",
        "kyc_status": "verified",
        "trust_score": 90,
        "bio": "Remote consultant renting workspaces, gaming consoles, bikes, and home essentials."
    },
    {
        "name": "Meera Sen (Event Designer)",
        "email": "customer.meera@rentzy.com",
        "phone": "+919866778899",
        "password": "Password@123",
        "role": "customer",
        "kyc_status": "verified",
        "trust_score": 93,
        "bio": "Wedding and corporate event stylist renting luxury items, occasion wear, and staging equipment."
    }
]

# 3 curated products for each of the 25 categories = 75 products
PRODUCTS_DATA = {
    "Electronics & Gadgets": [
        {"title": "Sony FX3 Full-Frame Cinema Camera Kit", "desc": "Cinema line camera with 24-70mm GM II lens, 2x 160GB CFexpress cards, and cage.", "loc": "Indiranagar, Bangalore", "pricing": {"hour": 350, "day": 2800, "week": 16000, "month": 55000}, "deposit": 12000, "img": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800&q=80"},
        {"title": "Apple MacBook Pro 16\" M3 Max (64GB)", "desc": "Heavy compute workstation for video rendering, 3D modeling and machine learning.", "loc": "HSR Layout, Bangalore", "pricing": {"hour": 250, "day": 2000, "week": 11000, "month": 38000}, "deposit": 15000, "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800&q=80"},
        {"title": "DJI Mavic 3 Pro Cine Drone with Smart Controller", "desc": "Triple camera Hasselblad optical system with ProRes recording and 43 min flight time.", "loc": "RS Puram, Coimbatore", "pricing": {"hour": 400, "day": 3200, "week": 18000, "month": 60000}, "deposit": 14000, "img": "https://images.unsplash.com/photo-1527977966376-1c8408f9f108?w=800&q=80"},
    ],
    "Bikes": [
        {"title": "Royal Enfield Himalayan 450 (Kamet White)", "desc": "Equipped with touring panniers, crash guards, and GPS phone mount. Fully serviced.", "loc": "Koramangala, Bangalore", "pricing": {"hour": 150, "day": 1200, "week": 7000, "month": 22000}, "deposit": 5000, "img": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=800&q=80"},
        {"title": "KTM Duke 390 Gen 3 Adventure Setup", "desc": "Dynamic cornering ABS, quickshifter+, and top box. Ideal for weekend mountain circuits.", "loc": "Gandhipuram, Coimbatore", "pricing": {"hour": 160, "day": 1300, "week": 7500, "month": 24000}, "deposit": 5500, "img": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=800&q=80"},
        {"title": "Trek Domane AL 4 Disc Road Cycle", "desc": "Lightweight alloy endurance road bike with Shimano Tiagra drivetrain and hydraulic disc brakes.", "loc": "Whitefield, Bangalore", "pricing": {"hour": 80, "day": 600, "week": 3200, "month": 9500}, "deposit": 3000, "img": "https://images.unsplash.com/photo-1485965120184-e220f721d03e?w=800&q=80"},
    ],
    "Cars": [
        {"title": "Mahindra Thar 4x4 Hard Top (Automatic)", "desc": "Rugged all-terrain lifestyle SUV equipped with off-road tires and Apple CarPlay.", "loc": "Indiranagar, Bangalore", "pricing": {"hour": 450, "day": 3500, "week": 21000, "month": 68000}, "deposit": 10000, "img": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?w=800&q=80"},
        {"title": "Hyundai Ioniq 5 Electric Long Range", "desc": "Ultra-fast charging luxury EV with ultra-quiet cabin, panoramic roof, and V2L power.", "loc": "Koramangala, Bangalore", "pricing": {"hour": 550, "day": 4500, "week": 27000, "month": 88000}, "deposit": 15000, "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&q=80"},
        {"title": "Toyota Innova Crysta ZX 7-Seater Luxury", "desc": "Captain seat diesel automatic, rear entertainment screens, ideal for family tours.", "loc": "Peelamedu, Coimbatore", "pricing": {"hour": 400, "day": 3200, "week": 19000, "month": 62000}, "deposit": 8000, "img": "https://images.unsplash.com/photo-1549399542-7e3f8b79c341?w=800&q=80"},
    ],
    "Rooms": [
        {"title": "Private Sunlit Creative Studio Room", "desc": "Acoustically treated studio room with high-speed 500Mbps fiber, ergonomic desk and attached bath.", "loc": "Indiranagar, Bangalore", "pricing": {"hour": 200, "day": 1400, "week": 8000, "month": 26000}, "deposit": 4000, "img": "https://images.unsplash.com/photo-1598928506311-c55ded91a20c?w=800&q=80"},
        {"title": "Executive Day-Use Meeting Suite", "desc": "Air-conditioned meeting room for 8 persons with 4K interactive display and video conference bar.", "loc": "MG Road, Bangalore", "pricing": {"hour": 350, "day": 2500, "week": 14000, "month": 45000}, "deposit": 3000, "img": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80"},
        {"title": "Cozy Garden-Facing Guest Room", "desc": "Quiet ensuite guest bedroom inside a heritage bungalow with garden access and breakfast inclusion.", "loc": "Race Course, Coimbatore", "pricing": {"hour": 150, "day": 1100, "week": 6500, "month": 21000}, "deposit": 2500, "img": "https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=800&q=80"},
    ],
    "PG Accommodations": [
        {"title": "Luxury Single Occupancy AC PG Room", "desc": "3 times chef-prepared meals, daily housekeeping, 1Gbps WiFi, biometric access, and gym.", "loc": "Electronic City Phase 1, Bangalore", "pricing": {"hour": 0, "day": 900, "week": 5500, "month": 18500}, "deposit": 10000, "img": "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=800&q=80"},
        {"title": "Premium Twin-Sharing Coliving Pod", "desc": "Individual study desks, private wardrobes, power backup, gaming lounge, and laundry.", "loc": "Koramangala 4th Block, Bangalore", "pricing": {"hour": 0, "day": 650, "week": 4000, "month": 13500}, "deposit": 8000, "img": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=800&q=80"},
        {"title": "Student & Professional PG Suite", "desc": "Fully furnished room close to tech parks with food, hot water, and secure parking.", "loc": "Saravanampatti, Coimbatore", "pricing": {"hour": 0, "day": 500, "week": 3200, "month": 10500}, "deposit": 6000, "img": "https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?w=800&q=80"},
    ],
    "Houses": [
        {"title": "3BHK Independent Luxury Villa with Lawn", "desc": "Gated society villa with private manicured lawn, modular kitchen, solar backup, and covered parking.", "loc": "Sarjapur Road, Bangalore", "pricing": {"hour": 0, "day": 4000, "week": 24000, "month": 75000}, "deposit": 30000, "img": "https://images.unsplash.com/photo-1580587771525-78b9dba3b914?w=800&q=80"},
        {"title": "Heritage Chettinad Courtyard Home", "desc": "Traditional heritage house for photo/film shoots, corporate offsites, and long family retreats.", "loc": "Pollachi Road, Coimbatore", "pricing": {"hour": 600, "day": 5500, "week": 32000, "month": 95000}, "deposit": 25000, "img": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&q=80"},
        {"title": "2BHK Modern Bungalow with Terrace Lounge", "desc": "Spacious living with private terrace garden, modular fittings, and 24/7 security guard.", "loc": "Vadavalli, Coimbatore", "pricing": {"hour": 0, "day": 2600, "week": 16000, "month": 48000}, "deposit": 20000, "img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800&q=80"},
    ],
    "Apartments": [
        {"title": "2BHK Fully Furnished High-Rise Flat", "desc": "24th floor panoramic city skyline view, infinity swimming pool access, clubhouse and tennis court.", "loc": "Bellandur, Bangalore", "pricing": {"hour": 0, "day": 2800, "week": 17000, "month": 52000}, "deposit": 25000, "img": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800&q=80"},
        {"title": "1BHK Scandinavian Loft Apartment", "desc": "Minimalist designer loft with smart lighting, dishwasher, home theatre, and balcony greenery.", "loc": "Indiranagar, Bangalore", "pricing": {"hour": 250, "day": 2200, "week": 13500, "month": 42000}, "deposit": 18000, "img": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800&q=80"},
        {"title": "3BHK Executive Flat near Tidal Park", "desc": "Gated community with gym, piped gas, standby generator, and dedicated two-car parking.", "loc": "Avinashi Road, Coimbatore", "pricing": {"hour": 0, "day": 2400, "week": 15000, "month": 44000}, "deposit": 20000, "img": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800&q=80"},
    ],
    "Land": [
        {"title": "1.5 Acre Gated Event Lawn & Open Space", "desc": "Level ground with perimeter lighting, 3-phase power grid connection, and parking for 120 cars.", "loc": "Yelahanka, Bangalore", "pricing": {"hour": 1500, "day": 12000, "week": 65000, "month": 220000}, "deposit": 25000, "img": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=800&q=80"},
        {"title": "5000 Sq.Ft Commercial Exhibition Plot", "desc": "Direct main road frontage plot suitable for seasonal popups, vehicle expos, and retail stalls.", "loc": "Avinashi Road, Coimbatore", "pricing": {"hour": 1000, "day": 8000, "week": 45000, "month": 150000}, "deposit": 20000, "img": "https://images.unsplash.com/photo-1628624747186-a941c476b7ef?w=800&q=80"},
        {"title": "Open Farm Plot for Camping & Film Sets", "desc": "Rustic agricultural scenic land with water source, coconut groves, and mountain view backdrop.", "loc": "Pollachi, Coimbatore", "pricing": {"hour": 800, "day": 6000, "week": 32000, "month": 100000}, "deposit": 15000, "img": "https://images.unsplash.com/photo-1500076656116-558758c991c1?w=800&q=80"},
    ],
    "Event & Party Equipment": [
        {"title": "JBL VRX Line Array Concert Sound System", "desc": "Complete dual line array with subwoofers, digital mixer, and Shure wireless microphones.", "loc": "Koramangala, Bangalore", "pricing": {"hour": 800, "day": 6500, "week": 35000, "month": 110000}, "deposit": 15000, "img": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=800&q=80"},
        {"title": "Full Stage DMX Moving Head Lighting Rig", "desc": "12x LED pars, 4x beam moving heads, haze machine, and wireless DMX controller board.", "loc": "Indiranagar, Bangalore", "pricing": {"hour": 600, "day": 4500, "week": 24000, "month": 80000}, "deposit": 10000, "img": "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=800&q=80"},
        {"title": "Inflatable 20ft Outdoor Cinema Projector & Screen", "desc": "High lumen laser projector, giant blower screen, and surround Bluetooth sound tower.", "loc": "RS Puram, Coimbatore", "pricing": {"hour": 400, "day": 3000, "week": 16000, "month": 50000}, "deposit": 7000, "img": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=800&q=80"},
    ],
    "Sports & Fitness Equipment": [
        {"title": "NordicTrack Commercial Treadmill 2450", "desc": "Interactive touchscreen with auto-incline, decline, and commercial grade shock absorption.", "loc": "Whitefield, Bangalore", "pricing": {"hour": 0, "day": 1200, "week": 5500, "month": 16000}, "deposit": 6000, "img": "https://images.unsplash.com/photo-1538805060514-97d9cc17730c?w=800&q=80"},
        {"title": "Olympic Barbell & Bumper Plate Set (150kg)", "desc": "Hard chrome needle-bearing bar, heavy duty rubber plates, squat stand, and locking collars.", "loc": "HSR Layout, Bangalore", "pricing": {"hour": 100, "day": 700, "week": 3200, "month": 9000}, "deposit": 4000, "img": "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=800&q=80"},
        {"title": "Concept2 Model D PM5 Indoor Rower", "desc": "The gold standard air resistance rowing machine with performance monitor and Bluetooth sync.", "loc": "Gandhipuram, Coimbatore", "pricing": {"hour": 0, "day": 900, "week": 4200, "month": 12500}, "deposit": 5000, "img": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=800&q=80"},
    ],
    "Travel & Camping Gear": [
        {"title": "Quechua 4-Person Blackout Air Tent + Camp Cots", "desc": "Fresh & Black inflatable tent, 2 foldable camping beds, lantern, and pump.", "loc": "Koramangala, Bangalore", "pricing": {"hour": 100, "day": 750, "week": 3800, "month": 11000}, "deposit": 3000, "img": "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=800&q=80"},
        {"title": "EcoFlow River 2 Max Portable Power Station 512Wh", "desc": "Powers laptops, cameras, mini coolers, and lights during wilderness off-grid trips.", "loc": "Indiranagar, Bangalore", "pricing": {"hour": 120, "day": 950, "week": 5000, "month": 15000}, "deposit": 5000, "img": "https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?w=800&q=80"},
        {"title": "Thule Motion XT XL Rooftop Cargo Box", "desc": "500L aerodynamic roof box with universal crossbar mount for long road expeditions.", "loc": "Race Course, Coimbatore", "pricing": {"hour": 80, "day": 650, "week": 3400, "month": 9800}, "deposit": 4000, "img": "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?w=800&q=80"},
    ],
    "Furniture": [
        {"title": "Herman Miller Aeron Ergonomic Task Chair", "desc": "Fully adjustable posturefit SL back support chair in graphite finish, size B.", "loc": "HSR Layout, Bangalore", "pricing": {"hour": 50, "day": 400, "week": 2200, "month": 6800}, "deposit": 5000, "img": "https://images.unsplash.com/photo-1580481077195-c3a821a506cb?w=800&q=80"},
        {"title": "Solid Sheesham Wood 6-Seater Dining Suite", "desc": "Handcrafted dining table with cushioned chairs and bench for staging and dining.", "loc": "Koramangala, Bangalore", "pricing": {"hour": 0, "day": 900, "week": 4500, "month": 13000}, "deposit": 6000, "img": "https://images.unsplash.com/photo-1617806118233-18e1de247200?w=800&q=80"},
        {"title": "Modern L-Shape Reversible Velvet Sofa", "desc": "Deep seated luxury corner sofa in emerald green velvet with accent throw cushions.", "loc": "Saibaba Colony, Coimbatore", "pricing": {"hour": 0, "day": 850, "week": 4200, "month": 12000}, "deposit": 5500, "img": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800&q=80"},
    ],
    "Home Appliances": [
        {"title": "LG 594L Side-by-Side Inverter Refrigerator", "desc": "Multi air flow with smart diagnosis, water dispenser, and ultra-quiet compressor.", "loc": "Bellandur, Bangalore", "pricing": {"hour": 0, "day": 800, "week": 4000, "month": 11500}, "deposit": 6000, "img": "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=800&q=80"},
        {"title": "Dyson V12 Detect Slim Cordless Vacuum", "desc": "Laser dust detection, HEPA filtration, and multiple motorized brush heads.", "loc": "Indiranagar, Bangalore", "pricing": {"hour": 70, "day": 500, "week": 2600, "month": 7500}, "deposit": 4000, "img": "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=800&q=80"},
        {"title": "Bosch 8kg Front Load Washing Machine", "desc": "EcoSilence drive, anti-vibration design, and 1400 RPM spin speed for fast drying.", "loc": "RS Puram, Coimbatore", "pricing": {"hour": 0, "day": 650, "week": 3300, "month": 9500}, "deposit": 5000, "img": "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=800&q=80"},
    ],
    "Tools": [
        {"title": "DeWalt 20V Max XR Brushless Combo Tool Kit", "desc": "Hammer drill, impact driver, circular saw, reciprocating saw, 2x 5Ah batteries.", "loc": "Peenya Industrial Area, Bangalore", "pricing": {"hour": 80, "day": 600, "week": 2800, "month": 8200}, "deposit": 3000, "img": "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=800&q=80"},
        {"title": "Makita Rotary Demolition Breaker Hammer (1500W)", "desc": "Anti-vibration technology concrete chipping hammer with SDS-Max chisels included.", "loc": "Gandhipuram, Coimbatore", "pricing": {"hour": 120, "day": 850, "week": 4200, "month": 12500}, "deposit": 4000, "img": "https://images.unsplash.com/photo-1581147036324-c17ac41dfa6c?w=800&q=80"},
        {"title": "Fluke 87V Industrial Digital Multimeter + Clamp", "desc": "True-RMS accuracy meter for industrial electronics, HVAC, and power diagnostics.", "loc": "Whitefield, Bangalore", "pricing": {"hour": 60, "day": 450, "week": 2200, "month": 6500}, "deposit": 2500, "img": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&q=80"},
    ],
    "Construction Equipment": [
        {"title": "Honda Petrol Concrete Vibrator + Screed Machine", "desc": "High frequency 4-stroke engine vibrator needle for high density slab casting.", "loc": "Hosur Road, Bangalore", "pricing": {"hour": 150, "day": 1100, "week": 5500, "month": 17000}, "deposit": 5000, "img": "https://images.unsplash.com/photo-1581094288338-2314dddb7ece?w=800&q=80"},
        {"title": "Mini Excavator Digging & Trenching Machine", "desc": "1.8 ton compact excavator with canopy, rubber tracks, and trenching bucket.", "loc": "Thudiyalur, Coimbatore", "pricing": {"hour": 800, "day": 6000, "week": 32000, "month": 110000}, "deposit": 20000, "img": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&q=80"},
        {"title": "Modular Heavy-Duty Steel Scaffolding Set (500 Sq.Ft)", "desc": "H-frames, cross braces, adjustable base jacks, and walk boards for multistory work.", "loc": "Peelamedu, Coimbatore", "pricing": {"hour": 0, "day": 1500, "week": 8000, "month": 24000}, "deposit": 8000, "img": "https://images.unsplash.com/photo-1541888946425-d0fbb186c5f8?w=800&q=80"},
    ],
    "Fashion & Occasion Wear": [
        {"title": "Sabyasachi Heritage Crimson Bridal Lehenga", "desc": "Hand-embroidered zardozi silk bridal lehenga with twin dupattas and preservation case.", "loc": "Indiranagar, Bangalore", "pricing": {"hour": 0, "day": 4500, "week": 18000, "month": 45000}, "deposit": 12000, "img": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&q=80"},
        {"title": "Raymond Made-to-Measure Midnight Tuxedo", "desc": "Pure Italian wool peak lapel tuxedo with pleated bib shirt, cufflinks and bow tie.", "loc": "Koramangala, Bangalore", "pricing": {"hour": 0, "day": 1800, "week": 7500, "month": 18000}, "deposit": 5000, "img": "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=800&q=80"},
        {"title": "Kanchipuram Pure Silk Bridal Saree (Gold Zari)", "desc": "Traditional handloom silk with rich pallu and contrasting designer embroidered blouse.", "loc": "RS Puram, Coimbatore", "pricing": {"hour": 0, "day": 1500, "week": 6000, "month": 15000}, "deposit": 4500, "img": "https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?w=800&q=80"},
    ],
    "Gaming Equipment": [
        {"title": "Sony PlayStation 5 Pro + 2 DualSense Controllers", "desc": "1TB SSD PS5 Pro bundled with FC 25, God of War Ragnarok, and charging dock.", "loc": "Koramangala, Bangalore", "pricing": {"hour": 90, "day": 650, "week": 3400, "month": 9800}, "deposit": 5000, "img": "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=800&q=80"},
        {"title": "Meta Quest 3 VR Headset (512GB) Bundle", "desc": "High-res mixed reality headset with Touch Plus controllers and Elite battery strap.", "loc": "HSR Layout, Bangalore", "pricing": {"hour": 100, "day": 750, "week": 3800, "month": 11000}, "deposit": 5500, "img": "https://images.unsplash.com/photo-1622979135225-d2ba269bc1df?w=800&q=80"},
        {"title": "Fanatec Gran Turismo DD Pro Racing Wheel Rig", "desc": "Direct drive force feedback wheel, load cell pedals, and foldable GT cockpit frame.", "loc": "Peelamedu, Coimbatore", "pricing": {"hour": 150, "day": 1200, "week": 6500, "month": 19000}, "deposit": 7000, "img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&q=80"},
    ],
    "Industrial Machinery": [
        {"title": "Kirloskar 25 kVA Silent Diesel Generator", "desc": "Soundproof acoustic canopy with AMF panel, fuel efficient and continuous duty rated.", "loc": "Peenya, Bangalore", "pricing": {"hour": 350, "day": 2600, "week": 14000, "month": 45000}, "deposit": 12000, "img": "https://images.unsplash.com/photo-1581092335397-9583fe92d232?w=800&q=80"},
        {"title": "Godrej 2.5 Ton Hydraulic Pallet Hand Truck", "desc": "Tandem polyurethane rollers, heavy duty steel chassis for warehouse freight handling.", "loc": "Gandhipuram, Coimbatore", "pricing": {"hour": 70, "day": 500, "week": 2500, "month": 7500}, "deposit": 3000, "img": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=800&q=80"},
        {"title": "Ingersoll Rand Two-Stage Industrial Air Compressor", "desc": "10 HP motor with 300L air receiver tank, continuous 175 PSI pressure output.", "loc": "Peelamedu, Coimbatore", "pricing": {"hour": 180, "day": 1300, "week": 6800, "month": 22000}, "deposit": 6000, "img": "https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=800&q=80"},
    ],
    "Gardening Tools": [
        {"title": "Stihl FS 120 Petrol Brushcutter & Trimmer", "desc": "High power 2-stroke grass cutter with metal blade and nylon head for estate maintenance.", "loc": "Whitefield, Bangalore", "pricing": {"hour": 70, "day": 500, "week": 2400, "month": 7000}, "deposit": 2500, "img": "https://images.unsplash.com/photo-1592417817098-8f3d6ef23a23?w=800&q=80"},
        {"title": "Karcher K7 Premium Smart Control Pressure Washer", "desc": "180 bar water jet cleaner with surface cleaner attachment for patios and exterior walls.", "loc": "Koramangala, Bangalore", "pricing": {"hour": 80, "day": 600, "week": 2900, "month": 8500}, "deposit": 3000, "img": "https://images.unsplash.com/photo-1617806118233-18e1de247200?w=800&q=80"},
        {"title": "Honda Self-Propelled Rotary Lawn Mower", "desc": "Twin blade steel deck lawn mower with grass collection bag and 7 height adjustments.", "loc": "Race Course, Coimbatore", "pricing": {"hour": 90, "day": 700, "week": 3400, "month": 9800}, "deposit": 3500, "img": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=800&q=80"},
    ],
    "Content Creation Equipment": [
        {"title": "Aputure 600d Pro LED Studio Light + Dome III", "desc": "Daylight balanced 600W COB light with wireless Sidus Link control and c-stand.", "loc": "Indiranagar, Bangalore", "pricing": {"hour": 150, "day": 1200, "week": 6500, "month": 21000}, "deposit": 6000, "img": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800&q=80"},
        {"title": "Rode RodeCaster Pro II Integrated Podcast Studio", "desc": "4 mic inputs, revolution preamps, SMART pads, and multitrack USB recording.", "loc": "HSR Layout, Bangalore", "pricing": {"hour": 100, "day": 800, "week": 4200, "month": 12500}, "deposit": 4000, "img": "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=800&q=80"},
        {"title": "DJI RS 3 Pro 3-Axis Gimbal Stabilizer", "desc": "Carbon fiber arms, automated axis locks, and LiDAR autofocus compatibility.", "loc": "RS Puram, Coimbatore", "pricing": {"hour": 90, "day": 700, "week": 3600, "month": 11000}, "deposit": 3500, "img": "https://images.unsplash.com/photo-1533750349088-cd871a92f312?w=800&q=80"},
    ],
    "Office & Business Equipment": [
        {"title": "Canon imageRUNNER ADVANCE Heavy Duty Multi-Copier", "desc": "High speed color laser print, copy, scan, duplexing, and network enterprise security.", "loc": "MG Road, Bangalore", "pricing": {"hour": 0, "day": 1500, "week": 7500, "month": 22000}, "deposit": 8000, "img": "https://images.unsplash.com/photo-1562774053-701939374585?w=800&q=80"},
        {"title": "BenQ 4K HDR High Brightness Conference Room Projector", "desc": "4000 ANSI lumens, wireless projection casting, and low-latency presentation mode.", "loc": "Electronic City, Bangalore", "pricing": {"hour": 120, "day": 900, "week": 4500, "month": 13500}, "deposit": 4500, "img": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=800&q=80"},
        {"title": "Fellowes AutoMax 200C Micro-Cut Paper Shredder", "desc": "Silent shredding of 200 sheets automatically into unreadable security particles.", "loc": "Avinashi Road, Coimbatore", "pricing": {"hour": 50, "day": 350, "week": 1800, "month": 5200}, "deposit": 2000, "img": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=800&q=80"},
    ],
    "Musical Instruments": [
        {"title": "Yamaha Clavinova CLP-745 Digital Piano", "desc": "GrandTouch-S wooden keys, Binaural CFX and Bosendorfer sampling, with bench.", "loc": "Indiranagar, Bangalore", "pricing": {"hour": 120, "day": 950, "week": 4800, "month": 14000}, "deposit": 6000, "img": "https://images.unsplash.com/photo-1520523839898-507127053c37?w=800&q=80"},
        {"title": "Fender American Professional II Stratocaster", "desc": "V-Mod II single-coil pickups, maple fretboard, hard shell flight case, and cable.", "loc": "Koramangala, Bangalore", "pricing": {"hour": 100, "day": 800, "week": 4000, "month": 12000}, "deposit": 5000, "img": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=800&q=80"},
        {"title": "Pearl Export Complete 5-Piece Drum Kit + Zildjian Cymbals", "desc": "Poplar shells, heavy duty chrome hardware stands, crash, ride, and hi-hats.", "loc": "RS Puram, Coimbatore", "pricing": {"hour": 150, "day": 1200, "week": 6000, "month": 18000}, "deposit": 6000, "img": "https://images.unsplash.com/photo-1519892300165-cb5542fb47c7?w=800&q=80"},
    ],
    "Hobby-Related Items": [
        {"title": "Celestron NexStar 8SE Computerized Telescope", "desc": "8-inch Schmidt-Cassegrain optics with motorized GoTo tracking of 40,000+ space objects.", "loc": "Sarjapur Road, Bangalore", "pricing": {"hour": 150, "day": 1200, "week": 6000, "month": 18000}, "deposit": 7000, "img": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800&q=80"},
        {"title": "Bambu Lab X1-Carbon Combo 3D Printer (with AMS)", "desc": "High speed multi-color 3D printing with carbon fiber filament capability and AI camera.", "loc": "HSR Layout, Bangalore", "pricing": {"hour": 120, "day": 950, "week": 4900, "month": 15000}, "deposit": 6000, "img": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&q=80"},
        {"title": "Bresser Professional Pottery Wheel Machine (350W)", "desc": "Smooth foot pedal speed regulation, 25cm turntable aluminum alloy wheel, sculpting tools.", "loc": "Race Course, Coimbatore", "pricing": {"hour": 80, "day": 600, "week": 3000, "month": 8800}, "deposit": 3500, "img": "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=800&q=80"},
    ],
    "Luxury Products": [
        {"title": "Rolex Submariner Date (Oystersteel 41mm)", "desc": "Original verified luxury timepiece in mint condition with insurance and original box.", "loc": "UB City, Bangalore", "pricing": {"hour": 500, "day": 4000, "week": 22000, "month": 70000}, "deposit": 25000, "img": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=800&q=80"},
        {"title": "Chanel Classic Double Flap Quilted Handbag", "desc": "Iconic black lambskin with gold metal chain hardware. Authentication cert provided.", "loc": "Lavelle Road, Bangalore", "pricing": {"hour": 350, "day": 2800, "week": 15000, "month": 48000}, "deposit": 18000, "img": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=800&q=80"},
        {"title": "Leica M11 Rangefinder Camera Body", "desc": "60MP BSI CMOS full-frame sensor, artisanal German brass build, with 35mm Summilux lens.", "loc": "Race Course, Coimbatore", "pricing": {"hour": 600, "day": 4800, "week": 26000, "month": 85000}, "deposit": 30000, "img": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800&q=80"},
    ],
    "Temporary Business Setups": [
        {"title": "Modular 10x10ft Trade Show Pavilion & Display Booth", "desc": "Custom printed backlit tension fabric counters, brochure stand, and LED spot lighting.", "loc": "BIEC / Yeshwanthpur, Bangalore", "pricing": {"hour": 300, "day": 2200, "week": 11000, "month": 34000}, "deposit": 7000, "img": "https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=800&q=80"},
        {"title": "Mobile Barista Espresso Cart & La Marzocco Machine", "desc": "Dual boiler commercial espresso maker, grinder, water filtration cart, for corporate events.", "loc": "Koramangala, Bangalore", "pricing": {"hour": 600, "day": 4500, "week": 23000, "month": 72000}, "deposit": 15000, "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800&q=80"},
        {"title": "Pop-up Retail Wooden Kiosk & POS Cash Drawer Setup", "desc": "Aesthetic collapsible timber retail island with shelf displays, tablet mount, and cash box.", "loc": "Brookefields Mall, Coimbatore", "pricing": {"hour": 250, "day": 1800, "week": 9000, "month": 28000}, "deposit": 6000, "img": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800&q=80"},
    ],
}

async def run_population():
    db = get_db()
    print("Starting Rentzy database population...")

    # 1. Update/Upsert Categories
    cat_map = {}
    for c in CATEGORIES:
        await db.categories.update_one(
            {"slug": c["slug"]},
            {"$set": {"name": c["name"], "icon": c["icon"], "active": True}},
            upsert=True
        )
        cat_doc = await db.categories.find_one({"slug": c["slug"]})
        cat_map[c["name"]] = str(cat_doc["_id"])
    print(f"Upserted {len(cat_map)} categories.")

    # 2. Register/Upsert Users
    user_map = {}
    for u in DEMO_USERS:
        email = u["email"].lower()
        update_data = {
            "name": u["name"],
            "email": email,
            "phone": u["phone"],
            "password_hash": hash_password(u["password"]),
            "role": u["role"],
            "kyc_status": u["kyc_status"],
            "trust_score": u["trust_score"],
            "bio": u["bio"],
            "blocked": False,
            "email_verified": True,
            "updated_at": datetime.now(timezone.utc)
        }
        await db.users.update_one(
            {"email": email},
            {"$set": update_data, "$setOnInsert": {"created_at": datetime.now(timezone.utc)}},
            upsert=True
        )
        u_doc = await db.users.find_one({"email": email})
        user_map[email] = str(u_doc["_id"])
        print(f"Registered user: {u['role']} - {u['name']} ({email})")

    owner_ids = [user_map[u["email"]] for u in DEMO_USERS if u["role"] == "owner"]

    # 3. Create at least 3 products per category (distributed among the 3 owners)
    total_added = 0
    now = datetime.now(timezone.utc)
    for cat_name, items in PRODUCTS_DATA.items():
        cat_id = cat_map[cat_name]
        for idx, item in enumerate(items):
            owner_id = owner_ids[idx % len(owner_ids)]
            product_filter = {"title": item["title"]}
            p_doc = {
                "owner_id": owner_id,
                "title": item["title"],
                "description": item["desc"],
                "category_id": cat_id,
                "category_name": cat_name,
                "images": [item["img"]],
                "location": item["loc"],
                "pricing": item["pricing"],
                "deposit": item["deposit"],
                "availability": "available",
                "status": "approved",
                "rules": "Handle with utmost care. Return in original clean state with all bundled items.",
                "updated_at": now
            }
            res = await db.products.update_one(
                product_filter,
                {"$set": p_doc, "$setOnInsert": {"created_at": now}},
                upsert=True
            )
            total_added += 1

    print(f"Total products populated/synced: {total_added}")

if __name__ == "__main__":
    asyncio.run(run_population())
