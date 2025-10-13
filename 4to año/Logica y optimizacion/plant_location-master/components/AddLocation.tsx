"use client";

import { useForm } from "react-hook-form";
import { Button } from "./ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "./ui/dialog";
import { Input } from "./ui/input";
import { DialogClose } from "@radix-ui/react-dialog";

const AddLocation = () => {
  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data: any) => {
    console.log(data);
    const response = await fetch("/api/location", {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    });
  };

  return (
    <Dialog>
      <div className="flex justify-end">
        <DialogTrigger asChild>
          <Button>Agregar Planta</Button>
        </DialogTrigger>
      </div>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Agregar Planta</DialogTitle>
          <DialogDescription>
            Complete la informacion requerida para añadir una nueva planta.
          </DialogDescription>
        </DialogHeader>
        <div className="py-2 items-center ">
          <form onSubmit={handleSubmit(onSubmit)}>
            <Input
              id="fixedCost"
              type="number"
              placeholder="Ingrese el costo fijo..."
              className="mb-2 py-2"
              {...register("cost", { required: true })}
            />
            <Input
              id="capacity"
              type="number"
              placeholder="Ingrese la capacidad..."
              className="mb-2 py-2"
              {...register("capacity", { required: true })}
            />
            <DialogClose>
              <Button type="submit">Agregar</Button>
            </DialogClose>
          </form>
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default AddLocation;
