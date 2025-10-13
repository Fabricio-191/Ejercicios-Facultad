"use client";

import { useForm } from "react-hook-form";
import { Button } from "./ui/button";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "./ui/dialog";
import { Input } from "./ui/input";

const Resolve = () => {
  const {
    register,
    handleSubmit,
    setValue,
    setResults,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data: any) => {
		const response = await fetch("/api/results", {
			method: "POST",
			body: JSON.stringify(data),
			headers: {
				"Content-Type": "application/json",
			},
		});

    fetch("/api/results")
      .then((res) => res.json())
      .then((data) => setResults(data.results))
      .catch(console.error);
  };

  return (
    <Dialog>
      <div className="flex justify-start my-4">
        <DialogTrigger asChild>
          <Button>Resolver Problema</Button>
        </DialogTrigger>
      </div>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Agregar un Nombre a tu problema</DialogTitle>
          <DialogDescription>
            Complete la informacion requerida para resolver un problema.
          </DialogDescription>
        </DialogHeader>
        <div className="py-2 items-center ">
          <form onSubmit={handleSubmit(onSubmit)}>
            <Input
              id="name"
              placeholder="Ingrese el Nombre"
              {...register("name", { required: true })}
            />
            <DialogFooter>
      				<DialogClose>
      					<Button type="submit" className="m-2">
      						Resolver
      					</Button>
      				</DialogClose>
            </DialogFooter>
          </form>
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default Resolve;
