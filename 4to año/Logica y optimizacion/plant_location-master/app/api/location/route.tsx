import { NextResponse } from "next/server";
import prisma from "@/db/prisma";

export async function GET() {
  try {
    const locations = await prisma.location.findMany({
      orderBy: { id: "desc" },
    });
    return NextResponse.json({ locations });
  } catch (error) {
    return NextResponse.json({ error: error });
  }
}

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { cost, capacity } = body;
    const location = await prisma.location.create({
      data: { fixedCost: Number(cost), capacity: Number(capacity) },
    });

    const clients = await prisma.client.findMany();
    for (const client of clients) {
      await prisma.locationClient.create({
        data: {
          clientId: client.id,
          locationId: location.id,
          cost: 0,
        },
      });
    }

    return NextResponse.json({ location });
  } catch (error) {
    return NextResponse.json({ error: error });
  }
}
