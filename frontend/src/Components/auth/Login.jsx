import React, { useState } from 'react'
import api from '../../api';

export const Login = () => {
    const [user,setUser]=useState({
        username:'',
        password:''
    })

    const handleChange=(e)=>{
        const {name,value}=e.target;
        setUser((prev)=>({
            ...prev,
            [name]:value
        }));
    }

    const handleSubmit=async(e)=>{
        e.preventDefault()
        
        try{
            const res=await api.post('auth/login/',user)
            alert(res.data.message)
        }
        catch (error) {
        alert(error.response.data['message']);
        }
        
    }
  return (
    <>
        <div>
            <form method='post' onSubmit={handleSubmit}>
                <div>
                    <label>Username</label>
                    <input type="text" value={user.username} name='username' onChange={handleChange} className='border rounded'/>
                </div>
                <div>
                    <label>Password</label>
                    <input type="text" value={user.password} name='password' onChange={handleChange} className='border rounded'/>
                </div>
                <button type='submit' className='border'>Login</button>
            </form>
        </div>
    </>
  )
}
