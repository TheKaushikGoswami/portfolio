import './App.css'
import Main from './components/Main'
import Home from './components/sub-components/Home'

import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

function App() {

  return (
    <>
    <Router>
      <Routes>
        <Route path="/" element={<Main />} >
          <Route path='/' element={<Home />} />
        </Route>
      </Routes>
    </Router>
    </>
  )
}

export default App
