import { GetServerSideProps } from "next";

export const getServerSideProps: GetServerSideProps = async () => {
  return {
    props: {
      BUILD_ENV: process.env.BUILD_ENV,
    },
  };
};

export default function Home({ BUILD_ENV }: { BUILD_ENV: string }) {
  return (
    <main className="flex flex-col items-center justify-center bg-[#FFFBF3] w-screen h-screen">
      <h1 className="text-7xl lg:text-[136px] font-gilroy font-bold text-[#FA4028]">
        Authentic
      </h1>
      <p className="text-stone-600">
        Running in <span className="text-[#FA4028] italic">{BUILD_ENV}</span>{" "}
        mode
      </p>
    </main>
  );
}
