import React, { useEffect, useState } from 'react';

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchDataFromBackend1 = async () => {
      const response = await fetch(process.env.REACT_APP_BACKEND1_URL);
      const result = await response.json();
      console.log(result.users);
    };

    const fetchDataFromBackend2 = async () => {
      const response = await fetch(process.env.REACT_APP_BACKEND2_URL);
      const result = await response.json();
      setUsers(result.users);
    };

    fetchDataFromBackend1();
    fetchDataFromBackend2();
  }, []);

  return (
    <div>
      <h1>Frontend 2</h1>
      <h2>Users from Backend 2:</h2>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.name} - {user.email}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
