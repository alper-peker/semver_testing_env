import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [lastUpdated, setLastUpdated] = useState(null)

  const loadData = async () => {
    setLoading(true)
    setError(null)

    try {
      const response = await fetch('/api/hello2')
      const json = await response.json()
      setData(json)
      setLastUpdated(new Date())
    } catch (err) {
      console.error('Hata:', err)
      setError(err)
      setData(null)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    loadData()
  }, [])

  const messageText = data?.message ?? data?.msg

  return (
    <div style={{ textAlign: 'center', padding: '50px', fontFamily: 'Arial' }}>
      <h1>Welcome to Test Environment of SEMVER 4 taico (FRONTEND V2)</h1>
      <div style={{ border: '2px solid #646cff', padding: '20px', borderRadius: '10px' }}>
        <h3>Backend Status:</h3>

        {loading ? (
          <p>Loading...</p>
        ) : error ? (
          <p style={{ color: 'red' }}>Could not connect to Backend</p>
        ) : data ? (
          <>
            <p style={{ color: 'green', fontSize: '1.2em', fontWeight: 'bold' }}>
              {messageText}
            </p>
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
