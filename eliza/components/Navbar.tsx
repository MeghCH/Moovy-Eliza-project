"use client";

import Link from "next/link";
import * as Tooltip from "@radix-ui/react-tooltip";
import {
  RiAddLargeLine,
  RiMenuSearchLine,
  RiChat1Line,
  RiUser3Line,
} from "@remixicon/react";

type NavLinkProps = {
  href: string;
  icon: React.ReactNode;
  label: string;
};

function NavLink({ href, icon, label }: NavLinkProps) {
  return (
    <Tooltip.Provider delayDuration={100}>
      <Tooltip.Root>
        <Tooltip.Trigger asChild>
          <Link
            href={href}
            className="text-gray-400 hover:text-purple-400 transition-colors"
          >
            {icon}
          </Link>
        </Tooltip.Trigger>
        <Tooltip.Portal>
          <Tooltip.Content
            side="right"
            sideOffset={12}
            className="bg-white/10 text-white text-xs px-3 py-1.5 rounded-lg backdrop-blur-sm border border-white/10"
          >
            {label}
            <Tooltip.Arrow className="fill-white/10" />
          </Tooltip.Content>
        </Tooltip.Portal>
      </Tooltip.Root>
    </Tooltip.Provider>
  );
}

export default function Navbar() {
  return (
    <nav className="fixed left-0 top-0 h-screen w-20 bg-white/5 border-r border-white/10 flex flex-col items-center py-8 gap-8 justify-between">
      <div className="flex flex-col gap-6 items-center">
        <Link
          href="/"
          className="text-purple-400 hover:text-purple-500 font-bold text-lg mb-4"
        >
          M
        </Link>
        <NavLink
          href="/chatbot"
          icon={<RiAddLargeLine size={22} />}
          label="Nouveau chat"
        />
        <NavLink
          href="/search"
          icon={<RiMenuSearchLine size={22} />}
          label="Rechercher"
        />
        <NavLink
          href="/recents"
          icon={<RiChat1Line size={22} />}
          label="Mes chats"
        />
      </div>
      <NavLink
        href="/profile"
        icon={<RiUser3Line size={22} />}
        label="Profil"
      />
    </nav>
  );
}
