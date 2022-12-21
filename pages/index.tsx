import Image from "next/image";

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center bg-[#FFFBF3] w-screen h-screen">
      <h1 className="text-7xl lg:text-[136px] font-gilroy font-bold text-[#FA4028]">
        Authentic
      </h1>
      <p className="text-stone-600">
        Running in{" "}
        <span className="text-[#FA4028] italic">{process.env.NODE_ENV}</span>{" "}
        mode
      </p>
    </main>
  );
}
