import { NextResponse } from "next/server";
import prisma from "@/db/prisma";

export async function PUT(
	request: Request,
	page: { params: { clientId: string } },
) {
	try {
		const { name, demand, custValue } = await request.json();
		const client = await prisma.client.update({
			where: { id: Number(page.params.clientId) },
			data: { name, demand, custValue },
		});
		return NextResponse.json({ client });
	} catch (error) {
		return NextResponse.json({ error: error });
	}
}

export async function DELETE(request: Request, page: { params: { clientId: string } }) {
	try {
		const client = await prisma.client.delete({
			where: { id: Number(page.params.clientId) },
		});
		return NextResponse.json({ client });
	} catch (error) {
		return NextResponse.json({ error: error });
	}
}
