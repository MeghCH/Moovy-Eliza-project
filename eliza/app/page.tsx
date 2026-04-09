import Features from "@/components/landing/Features";
import Header from "@/components/landing/Header";
import Demo from "@/components/landing/Demo";
import Results from "@/components/landing/Results";
import HowItWorks from "@/components/landing/HowItWorks";
import Footer from "@/components/landing/Footer";
import Divider from "@/components/landing/Divider";

export default function Home() {
  return (
    <main>
      <Header />
      <Divider />
      <Demo />
      <Divider />
      <Features />
      <Divider />
      <Results />
      <Divider />
      <HowItWorks />
      <Divider />
      <Footer />
    </main>
  );
}