import React from "react";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "MooVy - Ton assistant cinéma",
  description: "Trouve ton prochain film en 30 secondes",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="fr">
      <body className={`${inter.className} bg-[#0f0f0f] text-white`}>
        <Navbar />
        <div className="ml-20">{children}</div>
      </body>
    </html>
  );
}