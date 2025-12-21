import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/hello')
      .then(response => response.json())
      .then(json => {
        setData(json)
        setLoading(false)
      })
      .catch(err => {
        console.error("Hata:", err)
        setLoading(false)
      })
  }, [])

  return (
    <div style={{ textAlign: 'center', padding: '50px', fontFamily: 'Arial' }}>
      <h1>Welcome to Test Environment of SEMVER</h1>
      <div style={{ border: '2px solid #646cff', padding: '20px', borderRadius: '10px' }}>
        <h3>Backend Status:</h3>
        {loading ? (
          <p>Loading...</p>
        ) : data ? (
          <>
            <p style={{ color: 'green', fontSize: '1.2em', fontWeight: 'bold' }}>{data.message}</p>
            <small>Status: {data.status}</small>
          </>
        ) : (
          <p style={{ color: 'red' }}>Could not connect to Backend</p>
        )}
      </div>
    </div>
  )
}

export default App
