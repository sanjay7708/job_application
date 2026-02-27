import React, { useState } from 'react'

export const Login = () => {
    const [user,setUser]=useState({
        username:'',
        password:''
    })
  return (
    <>
        <div>
            <form method='post'>
                <div>
                    <label htmlFor="">Username</label>
                    <input type="text" value={user.username} onChange={(e)=>setUser((prev)=>e.target.value)} />
                </div>
            </form>
        </div>
    </>
  )
}
