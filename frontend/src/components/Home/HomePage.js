import React from 'react';
import '../w3.css';
import pic from '../../../static/images/python.png';

export default function HomePage() {
    return (
        <div className='w3-margin w3-padding' >
            <img src={pic} />
            <h1 className='w3-text-blue' >This Webapp is running UwU !</h1>
            <h2 className='uwu' >Now u can START working ;</h2>
        </div>
    );
}