"use client";

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
import { useRouter } from "next/navigation";
import { useForm } from "react-hook-form";

const AddClient = () => {
  const router = useRouter();

  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm();

  const onSubmit = (data: any) => {
    console.log(data);
    router.push(`/location/${data.demand}`);
  };

  return (
    <Dialog>
      <div className="flex justify-end">
        <DialogTrigger asChild>
          <Button>Agregar Cliente</Button>
        </DialogTrigger>
      </div>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Agregar Cliente</DialogTitle>
          <DialogDescription>
            Complete la informacion requerida para añadir un nuevo cliente.
          </DialogDescription>
        </DialogHeader>
        <div className="py-2 items-center ">
          <form onSubmit={handleSubmit(onSubmit)}>
            <Input
              id="demand"
              type="number"
              {...register("demand", { required: true })}
              placeholder="Ingrese la demanda..."
              className="mb-2"
            />
            <DialogFooter>
              <Button type="submit">Continuar</Button>
            </DialogFooter>
          </form>
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default AddClient;
