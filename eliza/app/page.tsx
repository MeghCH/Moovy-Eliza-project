import Features from "@/components/Features";
import Header from "@/components/Header";
import Demo from "@/components/Demo";
import Results from "@/components/Results";
import HowItWorks from "@/components/HowItWorks";
import Footer from "@/components/Footer";
import Divider from "@/components/Divider";

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