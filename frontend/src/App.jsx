import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { BrowserRouter,Routes,Route } from 'react-router-dom'
import { Login } from './Components/auth/Login'


function App() {
  

  return (
    <>
     <BrowserRouter>
      <Routes>
        <Route path='/' element={<Login/>}/>
      </Routes>
     </BrowserRouter>
    </>
  )
}

export default App
