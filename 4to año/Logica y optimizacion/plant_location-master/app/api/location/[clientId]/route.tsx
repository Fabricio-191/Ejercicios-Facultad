import { NextResponse } from "next/server";
import prisma from "@/db/prisma";

export async function GET(request: Request, { params }: { params: { clientId: string } }) {
	try {
		const clientLocations = await prisma.locationClient.findMany({
			where: { clientId: Number(params.clientId) },
		});
		return NextResponse.json({ clientLocations });
	} catch (error) {
		return NextResponse.json({ error: error });
	}
}

export async function PUT(request: Request, page: { params: { clientId: string } }) {
  try {
    const data = await request.json();
    const client = await prisma.locationClient.update({
      where: { id: Number(page.params.clientId) },
      data,
    });
    return NextResponse.json({ client });
  } catch (error) {
    return NextResponse.json({ error: error });
  }
}
