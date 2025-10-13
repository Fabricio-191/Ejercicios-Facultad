"use client";
import EditLocationClient from "@/components/EditLocationClient";
import MaxWidthWrapper from "@/components/MaxWidthWrapper";
import { Button } from "@/components/ui/button";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { useEffect, useState } from "react";
import { LocationClient } from "@prisma/client";

type PageProps = { params: { clientId: string } };

export default function Page({ params }: PageProps) {
  const [locationClients, setClients] = useState<LocationClient[]>([]);

  useEffect(() => {
    fetch("/api/location/" + params.clientId, { method: "GET" })
      .then((res) => res.json())
      .then((data) => setClients(data.clientLocations))
      .catch(console.error);
  }, [params.clientId]);

  return (
    <MaxWidthWrapper>
      <div className="my-2">
        <h1 className="text-3xl font-bold font-sans  text-slate-500">
          Cliente {params.clientId}
        </h1>
        <h1 className="text-3xl font-semibold font-sans text-slate-500">
          Plantas{" "}
        </h1>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Planta</TableHead>
              <TableHead>Costo</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {locationClients.map((locationClient) => (
              <TableRow key={locationClient.id}>
                <TableCell>{locationClient.locationId}</TableCell>
                <TableCell>{locationClient.cost}</TableCell>
                <EditLocationClient
                  id={locationClient.locationId}
                  name={locationClient.locationId.toString()}
                  cost={locationClient.cost}
                ></EditLocationClient>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </MaxWidthWrapper>
  );
}
