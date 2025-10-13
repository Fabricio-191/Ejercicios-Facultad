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

const EditLocationClient = ({
  id,
  name,
  cost,
}: {
  id: number;
  name: string;
  cost: number;
}) => {
  const router = useRouter();

  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm();

  const onSubmit = (data: any) => {
    console.log(data);
    alert("Costo cambiado");
  };

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline">Editar</Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Cambiar Costo</DialogTitle>
          <DialogDescription>
            Ingrese el nuevo costo para la planta {name}.
          </DialogDescription>
        </DialogHeader>
        <div className="py-2 items-center ">
          <form onSubmit={handleSubmit(onSubmit)}>
            <Input
              id="cost"
              type="number"
              {...register("cost", { required: true })}
              placeholder="Ingrese el costo..."
              className="mb-2"
            />
            <DialogFooter>
              <Button type="submit">Guardar</Button>
            </DialogFooter>
          </form>
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default EditLocationClient;
