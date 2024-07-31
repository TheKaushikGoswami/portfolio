import React from 'react';
import Link from 'next/link';

const Navbar = () => (
  <nav>
    <ul>
      <li><Link href="/"><a>Home</a></Link></li>
      <li><Link href="/about"><a>About</a></Link></li>
      <li><Link href="/skills"><a>Skills</a></Link></li>
      <li><Link href="/projects"><a>Projects</a></Link></li>
      <li><Link href="/contact"><a>Contact</a></Link></li>
    </ul>
  </nav>
);

export default Navbar;
