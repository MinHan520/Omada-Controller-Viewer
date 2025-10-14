import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [message, setMessage] = useState('')

  useEffect(() => {
    axios.get('http://localhost:8000/')
      .then((response) => {
        setMessage(response.data.message)
      })
      .catch((error) => {
        setMessage('Failed to connect to backend')
    })
  }, [])

  return (
    <div>
      <h1>Backend says:</h1>
      <p>{message}</p>
    </div>
  )
}

export default App;
