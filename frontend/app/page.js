export default async function Home() {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL || "https://ktm-rental-api.onrender.com";
  
  let listings = [];
  try {
    const res = await fetch(`${apiUrl}/listings`, { cache: 'no-store' });
    if (res.ok) {
      listings = await res.json();
    }
  } catch (err) {
    console.error("Failed to fetch listings:", err);
  }

  return (
    <main style={{ padding: '2rem', fontFamily: 'sans-serif', maxWidth: '800px', margin: '0 auto' }}>
      <h1>Kathmandu Valley Rentals</h1>
      <p style={{ color: '#666' }}>Verified No-Broker Rental Properties</p>

      <hr style={{ margin: '1.5rem 0' }} />

      <h2>Available Listings</h2>
      {listings.length === 0 ? (
        <p>Loading or no listings available...</p>
      ) : (
        listings.map((item) => (
          <div key={item.id} style={{ border: '1px solid #ccc', borderRadius: '8px', padding: '1rem', marginBottom: '1rem' }}>
            <h3>{item.title}</h3>
            <p><strong>Location:</strong> {item.location}</p>
            <p><strong>Price:</strong> NPR {item.price} / month</p>
            <p><strong>Floor:</strong> {item.floor_level}</p>
            <p><strong>Water Supply:</strong> {item.water_facility}</p>
            <p><strong>Direct Owner:</strong> {item.is_verified_owner ? "Yes (Verified)" : "No"}</p>
          </div>
        ))
      )}
    </main>
  );
}