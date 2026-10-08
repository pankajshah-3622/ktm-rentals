'use client';
import { useState } from 'react';

export default function AddListing() {
  const [formData, setFormData] = useState({
    title: '',
    location: '',
    price: '',
    floor_level: '1st Floor',
    water_facility: 'Melamchi + Underground Tanker',
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const apiUrl = process.env.NEXT_PUBLIC_API_URL || "https://ktm-rental-api.onrender.com";

    const res = await fetch(`${apiUrl}/listings`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ...formData,
        price: parseFloat(formData.price),
        parking_available: true,
        is_verified_owner: true
      }),
    });

    if (res.ok) {
      alert('Listing created successfully!');
      window.location.href = '/';
    } else {
      alert('Failed to create listing.');
    }
  };

  return (
    <main style={{ padding: '2rem', fontFamily: 'sans-serif', maxWidth: '600px', margin: '0 auto' }}>
      <h1>Post a New Rental Listing</h1>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        <input 
          placeholder="Title (e.g. 3 BHK Flat in Jhamsikhel)" 
          required 
          onChange={(e) => setFormData({...formData, title: e.target.value})}
          style={{ padding: '0.5rem' }}
        />
        <input 
          placeholder="Location (e.g. Lalitpur, Baneshwor)" 
          required 
          onChange={(e) => setFormData({...formData, location: e.target.value})}
          style={{ padding: '0.5rem' }}
        />
        <input 
          placeholder="Monthly Rent (NPR)" 
          type="number" 
          required 
          onChange={(e) => setFormData({...formData, price: e.target.value})}
          style={{ padding: '0.5rem' }}
        />
        <select onChange={(e) => setFormData({...formData, floor_level: e.target.value})} style={{ padding: '0.5rem' }}>
          <option>Ground Floor</option>
          <option>1st Floor</option>
          <option>2nd Floor</option>
          <option>Top Floor</option>
        </select>
        <button type="submit" style={{ padding: '0.75rem', background: '#0070f3', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
          Submit Listing
        </button>
      </form>
    </main>
  );
}