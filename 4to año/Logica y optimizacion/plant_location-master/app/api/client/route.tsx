import { NextResponse } from "next/server";
import prisma from "@/db/prisma";
import { Location } from "@prisma/client";

export async function GET() {
	try {
		const clients = await prisma.client.findMany({
			orderBy: { id: "desc" },
		});
		return NextResponse.json({ clients });
	} catch (error) {
		return NextResponse.json({ error: error });
	}
}

export async function POST(request: Request) {
	try {
		const { name, demand, custValue } = await request.json();

		const client = await prisma.client.create({
			data: { name, demand, custValue },
		});

		const location = await prisma.location.findMany();

		location.map(async (location: Location) => {
			await prisma.locationClient.create({
				data: {
					clientId: client.id,
					locationId: location.id,
					cost: 0,
				},
			});
		});

		return NextResponse.json({ client });
	} catch (error) {
		return NextResponse.json({ error });
	}
}
