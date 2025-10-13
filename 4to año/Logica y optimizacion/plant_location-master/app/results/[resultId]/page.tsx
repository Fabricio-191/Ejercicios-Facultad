"use client";
import { useEffect, useState } from "react";
import { Results } from "@prisma/client";
import MaxWidthWrapper from "@/components/MaxWidthWrapper";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import {
	Table,
	TableBody,
	TableCell,
	TableHead,
	TableHeader,
	TableRow,
} from "@/components/ui/table";

export default function Page(pageProp: { params: { resultId: number } }) {
	const [result, setResult] = useState<Results | null>(null);

	useEffect(() => {
		fetch("/api/results/" + pageProp.params.resultId, { method: "GET" })
			.then((res) => res.json())
			.then((data) => {
				setResult(data.results);
			})
			.catch(console.error);
	}, [pageProp.params.resultId]);

	if (!result) {
		return (
			<MaxWidthWrapper>
				<div>
					<p>Cargando...</p>
				</div>
			</MaxWidthWrapper>
		);
	}

	const solutionData = JSON.parse(result.solutionData);
	const inputData = JSON.parse(result.inputdata);

	return (
		<MaxWidthWrapper className="">
			<div className="flex flex-col items-center justify-center w-full h-full p-4 space-y-4">
				<h1 className="text-3xl font-bold font-sans text-slate-500">
					{result.name}
				</h1>
				<h2 className="text-2xl font-semibold font-sans text-slate-500">
					Fecha de creacion:{" "}
					{new Date(result.createdAt).toLocaleString()}
				</h2>
				<div>
					<Tabs defaultValue="results" className="w-full">
						<TabsList className="flex items-center">
							<TabsTrigger value="solutionLocation">
								Plantas
							</TabsTrigger>
							<TabsTrigger value="solutionCustomer">
								Clientes
							</TabsTrigger>
							<TabsTrigger value="solutionValues">
								Valores de solucion
							</TabsTrigger>
							<TabsTrigger value="inputs">Entrada</TabsTrigger>
							<TabsTrigger value="console">Consola</TabsTrigger>
						</TabsList>
						<TabsContent value="solutionLocation">
							<h3 className="text-lg font-bold font-sans text-slate-500">
								Estado de las plantas
							</h3>
							<Table>
								<TableHeader>
									<TableRow>
										<TableHead>Planta</TableHead>
										<TableHead>Load</TableHead>
										<TableHead>Open</TableHead>
									</TableRow>
								</TableHeader>
								<TableBody>
									{solutionData.solutionLocation.map(
										(
											loc: {
												location: number;
												load: number;
												open: number;
											},
											index: number,
										) => (
											<TableRow key={index}>
												<TableCell>
													{loc.location + 1}
												</TableCell>
												<TableCell>
													{loc.load}
												</TableCell>
												<TableCell>
													{loc.open === 1
														? "Abierta"
														: "Cerrada"}
												</TableCell>
											</TableRow>
										),
									)}
								</TableBody>
							</Table>
						</TabsContent>

						<TabsContent value="solutionCustomer">
							<h3 className="text-lg font-bold font-sans text-slate-500">
								Asignacion de plantas para cada cliente
							</h3>
							<Table>
								<TableHeader>
									<TableRow>
										<TableHead>Cliente</TableHead>
										<TableHead>Planta asignada</TableHead>
									</TableRow>
								</TableHeader>
								<TableBody>
									{solutionData.solutionCustomer.map(
										(
											cust: {
												cust: number;
												location: number;
											},
											index: number,
										) => (
											<TableRow key={index}>
												<TableCell>
													{cust.cust + 1}
												</TableCell>
												<TableCell>
													{cust.location}
												</TableCell>
											</TableRow>
										),
									)}
								</TableBody>
							</Table>
						</TabsContent>

						<TabsContent value="solutionValues">
							<h3 className="text-lg font-bold font-sans text-slate-500">
								Otros valores de la solucion
							</h3>
							<Table>
								<TableHeader>
									<TableRow>
										<TableHead>Objective</TableHead>
										<TableHead>Occupancy</TableHead>
										<TableHead>Min Occupancy</TableHead>
									</TableRow>
								</TableHeader>
								<TableBody>
									{solutionData.solutionValues.map(
										(
											val: {
												obj: number;
												occupancy: number;
												minOccup: number;
											},
											index: number,
										) => (
											<TableRow key={index}>
												<TableCell>{val.obj}</TableCell>
												<TableCell>
													{val.occupancy}
												</TableCell>
												<TableCell>
													{val.minOccup}
												</TableCell>
											</TableRow>
										),
									)}
								</TableBody>
							</Table>
						</TabsContent>

						<TabsContent value="inputs">
							<div className="flex flex-col justify-center items-center">
								<h3 className="mb-3 text-xl text-center font-bold font-sans text-slate-500">
									Datos de entrada
								</h3>
								<p className="w-3/4 mx-10 px-5 overflow-scroll">{JSON.stringify(inputData)}</p>
							</div>
						</TabsContent>

						<TabsContent value="console">
							<h3 className="text-xl font-bold font-sans text-slate-500">
								Salida de la consola
							</h3>
							<pre className="bg-black text-green-500 p-4 rounded font-mono whitespace-pre-wrap">
								{result.console}
							</pre>
						</TabsContent>
					</Tabs>
				</div>
			</div>
		</MaxWidthWrapper>
	);
}
