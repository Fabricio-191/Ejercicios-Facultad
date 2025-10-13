"use client";
import MaxWidthWrapper from "@/components/MaxWidthWrapper";
import Link from "next/link";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Button } from "@/components/ui/button";
import { Trash2 } from "lucide-react";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import AddClient from "@/components/AddClient";
import AddLocation from "@/components/AddLocation";
import Resolve from "@/components/Resolve";
import { useEffect, useState } from "react";
import { Client, Location, LocationClient, Result } from "@prisma/client";

function deleteResult(id: string, setResults: any) {
  return async () => {
    const response = await fetch("/api/results/" + id, {
      method: "DELETE",
    });

    if (response.ok) {
      const newResults = await fetch("/api/results")
        .then((res) => res.json())
        .then((data) => data.results)
        .catch(console.error);
      setResults(newResults);
    }
  };
}

function deleteLocation(id: number, setLocations: any) {
  return async () => {
    const response = await fetch("/api/location/" + id, { method: "DELETE" });

    if (response.ok) {
      const newLocations = await fetch("/api/location")
        .then((res) => res.json())
        .then((data) => data.locations)
        .catch(console.error);
      setLocations(newLocations);
    }
  };
}

function deleteClient(id: string, setClients: any) {
  return async () => {
    const response = await fetch("/api/client/" + id, { method: "DELETE" });

    if (response.ok) {
      const newClients = await fetch("/api/client")
        .then((res) => res.json())
        .then((data) => data.clients)
        .catch(console.error);
      setClients(newClients);
    }
  };
}

export default function Home() {
  const [locations, setLocations] = useState<Location[]>([]);
  const [clients, setClients] = useState<Client[]>([]);
  const [results, setResults] = useState<Result[]>([]);

  useEffect(() => {
    fetch("/api/location")
      .then((res) => res.json())
      .then((data) => setLocations(data.locations))
      .catch(console.error);
  }, []);

  useEffect(() => {
    fetch("/api/client")
      .then((res) => res.json())
      .then((data) => setClients(data.clients))
      .catch(console.error);
  }, []);

  useEffect(() => {
    fetch("/api/results")
      .then((res) => res.json())
      .then((data) => setResults(data.results))
      .catch(console.error);
  }, []);

  return (
    <MaxWidthWrapper className="">
      <div className="flex flex-col items-center justify-center w-full h-full p-4 space-y-4">
        <Tabs defaultValue="locations" className="w-full">
          <TabsList className="flex items-center">
            <TabsTrigger value="locations" className="w-1/2">
              Plantas
            </TabsTrigger>
            <TabsTrigger value="clients" className="w-1/2">
              Clientes
            </TabsTrigger>
            <TabsTrigger value="results" className="w-1/2">
              Resultados
            </TabsTrigger>
          </TabsList>
          <TabsContent value="locations">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Numero</TableHead>
                  <TableHead>Costo Fijo</TableHead>
                  <TableHead>Capacidad</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {locations.map((location) => (
                  <TableRow key={location.id}>
                    <TableCell>{location.id}</TableCell>
                    <TableCell>{location.fixedCost}</TableCell>
                    <TableCell>{location.capacity}</TableCell>
                    <TableCell>
                      <Button
                        onClick={deleteLocation(location.id, setLocations)}
                        variant="destructive"
                      >
                        <Trash2 />
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
            {/* Agrega una nueva planta */}
            <AddLocation />
          </TabsContent>
          <TabsContent value="clients">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Numero</TableHead>
                  <TableHead>Demanda</TableHead>
                  <TableHead>Plantas</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {clients.map((client) => (
                  <TableRow key={client.id}>
                    <TableCell>{client.id}</TableCell>
                    <TableCell>{client.demand}</TableCell>
                    <TableCell>
                      <Button variant="outline">
                        <Link href={`/location/${client.id}`}>Administrar</Link>
                      </Button>
                    </TableCell>
                    <TableCell>
                      <Button
                        onClick={deleteClient(client.id, setClients)}
                        variant="destructive"
                      >
                        <Trash2 />
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
            {/* Agrega un nuevo cliente */}
            <AddClient />
          </TabsContent>
          <TabsContent value="results">
            <Resolve setResults={setResults} />
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Nombre</TableHead>
                  <TableHead>Resultado</TableHead>
                  <TableHead>Estado de la Solucion</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {results.map((result) => (
                  <TableRow key={result.id}>
                    <TableCell>{result.name}</TableCell>
                    <TableCell>
                      {JSON.parse(result.solutionData).solutionValues[0].obj}
                    </TableCell>
                    <TableCell>{result.statusSolution}</TableCell>
                    <TableCell>
                      {new Date(result.createdAt).toLocaleString()}
                    </TableCell>
                    <TableCell>
                      <Link
                        key={result.id}
                        href={`/results/${result.id}`}
                        className="hover:cursor-pointer"
                      >
                        <Button>Ver Detalles</Button>
                      </Link>
                    </TableCell>
                    <TableCell>
                      <Button
                        onClick={deleteResult(result.id, setResults)}
                        variant="destructive"
                      >
                        <Trash2 />
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TabsContent>
        </Tabs>
      </div>
    </MaxWidthWrapper>
  );
}
