"use client";
import Image from "next/image";
import { use, useEffect, useState } from "react";

export default function Home() {
  const [data, setData] = useState<any[]>([]);
  
  useEffect(() => {
    fetch('http://127.0.0.1:5000/random-buy', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ side: 'CT', money: 800 }),
    })
    .then(response => response.json())
    .then(data => setData(data))
    .catch(error => console.error('Error fetching data:', error));
  }, []);

  console.log(data);
  return (

    <div>
      {data ? (
      data.map((data: any, index : number) => (
        <li key ={index} className="text-3xl font-bold underline">
          {data.item  }
          {data.price }
        </li>
      ))
      ) : "Loading..."}
    </div>
  );
}
