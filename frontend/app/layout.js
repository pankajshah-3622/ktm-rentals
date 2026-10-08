export const metadata = {
  title: 'Kathmandu Rentals',
  description: 'No-broker rental marketplace for Kathmandu Valley',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}