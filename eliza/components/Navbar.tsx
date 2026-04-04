import Link from "next/link";
import {
  RiAddLargeLine,
  RiMenuSearchLine,
  RiChat1Line,
  RiUser3Line,
} from "@remixicon/react";

export default function Navbar() {
  return (
    <nav className="fixed left-0 top-0 h-screen w-20 bg-white/5 border-r border-white/10 flex flex-col items-center py-8 gap-8 justify-between ">
      <div className="flex flex-col gap-6 items-center">
        <Link href="/" className="text-purple-400 font-bold text-lg mb-4">
          M
        </Link>
        <Link
          href="/chatbot"
          className="text-gray-400 hover:text-purple-400 transition-colors"
        >
          <RiAddLargeLine size={22} />
        </Link>
        <Link
          href="/search"
          className="text-gray-400 hover:text-purple-400 transition-colors"
        >
          <RiMenuSearchLine size={22} />
        </Link>
        <Link
          href="/chats"
          className="text-gray-400 hover:text-purple-400 transition-colors"
        >
          <RiChat1Line size={22} />
        </Link>
      </div>
      <Link
        href="/profile"
        className="text-gray-400 hover:text-purple-400 transition-colors"
      >
        <RiUser3Line size={22} />
      </Link>
    </nav>
  );
}