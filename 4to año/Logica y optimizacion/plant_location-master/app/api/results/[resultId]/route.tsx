import { NextRequest, NextResponse } from "next/server";
import prisma from "@/db/prisma";

export async function GET(
	request: NextRequest,
	page: { params: { resultId: string } },
) {
	try {
		const results = await prisma.results.findUniqueOrThrow({
			where: { id: Number(page.params.resultId) },
		});
		return NextResponse.json({ results });
	} catch (error) {
		return NextResponse.json({ error });
	}
}

export async function DELETE(
	request: NextRequest,
	page: { params: { resultId: string } },
) {
	try {
		const data = await prisma.results.delete({
			where: { id: Number(page.params.resultId) },
		});
		return NextResponse.json({ message: "Deleted", data });
	} catch (error) {
		return NextResponse.json({ error });
	}
}
