import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./NavBar";
import Login from "../pages/Login";

function App() {

  return (
    <h1>Project Client App</h1>
  );
}
export default App;

//   const [user, setUser] = useState(null);

//   useEffect(() => {
//     // auto-login
//     fetch("/check_session").then((r) => {
//       if (r.ok) {
//         r.json().then((user) => setUser(user));
//       }
//     });
//   }, []);

//   if (!user) return <Login onLogin={setUser} />;

//   // return <h1>Project Client</h1>;
//   return (
//     <Router>
//       <NavBar user={user} setUser={setUser} />
//       <Routes>
//         <Route path="/" element={<Favorite />} />
//         <Route path="/users" element={<User />} />
//         <Route path="/businesses" element={<Business />} />
//         <Route path="/listings" element={<Listing />} />
//         <Route path="/bookings" element={<Booking />} />
//         <Route path="/reviews" element={<Review />} />
//         <Route path="/login" element={<Login />} />
//         <Route path="/signup" element={<SignUpForm />} /> 
//         <Route path="*" element={<NotFound />} />
//       </Routes>
//     </Router>
//   );
// }

// export default App;
